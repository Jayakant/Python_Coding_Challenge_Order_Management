from dao.IOrderManagementRepository import IOrderManagementRepository
# from exceptions import UserNotFoundException, OrderNotFoundException
from exception.UserNotFoundException import UserNotFoundException
from exception.UserAlreadyExists import *
from exception.ProductAlreadyExists import *
from exception.OrderNotFound import *
from exception.OrderAlreadyExists import *
from exception.ProductNotFoundException import *
class OrderProcessor(IOrderManagementRepository):
    def __init__(self):
        pass
    
    def create_order(self, conn):
        cursor = conn.cursor()

        try:
            orderId = int(input("Enter orderId "))
            orderData = cursor.execute("select * from Orders where orderId=?",(orderId)).fetchone()
            if(orderData!= None):
                raise OrderAlreadyExists()
            userId = int(input("Enter userId "))
            userData = cursor.execute("select * from Users where userId=?",(userId)).fetchone()
            if(userData == None):
                raise UserNotFoundException()
            productId = int(input("Enter productId "))
            productData = cursor.execute("select * from Product where productId=?",(productId)).fetchone()
            if(productData == None):
                raise ProductNotFoundException()
            cursor.execute("insert into Orders values(?,?,?)",(orderId,userId,productId))
            conn.commit()
            print(f"Created order {orderId} successfully ")
        except Exception as e:
            print(f"Error {e}")
        
    def cancel_order(self, conn):
        try:
            cursor = conn.cursor()
            orderId = int(input("Enter orderId to cancel "))
            orderData = cursor.execute("select * from Orders where orderId=?",(orderId)).fetchone()
            if(orderData == None):
                raise OrderNotFound()
            cursor.execute("delete from Orders where orderId=?",(orderId))
            conn.commit()
            print(f"Removed order {orderId} successfully! ")
        except OrderNotFound as e:
            print(f"Error {e}")
    
    def create_product(self, conn):
        
        try:
            cursor = conn.cursor()
            productId = int(input("Enter productId "))
            productData = cursor.execute("select * from Product where productId=?",(productId)).fetchone()
            if(productData != None):
                raise ProductAlreadyExists()
            productName = input("Enter productName ")
            description = input("Enter description ")
            price = round(float(input("Enter price ")),2)
            quantityInStock = int(input("Enter quantity in stock "))
            type = input("Enter product type ")
            
            cursor.execute("insert into Product values(?,?,?,?,?,?)",(productId,productName,description,price,quantityInStock,type))
            conn.commit()
            print(f"Created product {productName} successfulyy! ")
        except ProductAlreadyExists as e:
            print(f"Error {e}")
    
    def create_user(self, conn):
        
        try:
            cursor = conn.cursor()
            userId = int(input("Enter userId "))
            userData = cursor.execute("select * from Users where userId=?",(userId)).fetchone()
            if(userData != None):
                raise UserAlreadyExists()
            userName = input("Enter userName ")
            password = input("Enter password ")
            role = input("Enter role ")
            cursor.execute("insert into Users values(?,?,?,?)",(userId,userName,password,role))
            
            conn.commit()
            print(f"User {userName} created successfully! ")
        except UserAlreadyExists as e:
            print(f"\nError {e}")
    
    def get_all_products(self, conn):
        cursor = conn.cursor()
        products = list(cursor.execute("select * from Product").fetchall())
        return products
    
    def get_order_by_user(self, conn):
        try:
            cursor = conn.cursor()
            userId = int(input("Enter userId "))
            userData = cursor.execute("select * from Users where userId=?",(userId)).fetchone()
            if(userData == None):
                raise UserNotFoundException()
            orders = list(cursor.execute("select * from Orders where userId=?",(userId)).fetchall())
            return orders
        except UserNotFoundException as e:
            print(f"\nError {e}")
        
