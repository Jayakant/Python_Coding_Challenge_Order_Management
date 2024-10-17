import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from util.DBPropertyUtil import *
from util.DBConnUtil import *
from dao.OrderProcessor import *

class MainModule:
    def menu():
        orderProcessorObj = OrderProcessor()
        connStr = DBPropertyUtil.getConnectionStr()
        conn = DBConnUtil.getConnObj(connStr)
        cursor = conn.cursor()
        
        usersList = cursor.execute("select * from Users").fetchall()
        
        isUserLoggedIn = False

        userName = input("Enter userName if you are an existing user ")
        # isUserLoggedIn = False
        userDetails = None
        for tup in usersList:
            if(tup[1] == userName):
                userDetails = tup
        if(userDetails != None):
            while(True):
                password = input("Enter Password or pass to exit ")
                if(password == ""):
                    break
                if(password == userDetails[2]):
                    isUserLoggedIn = True
                    print("Access granted ")
                    break
                else:
                    print("Incorrect password ")
                
        if(not isUserLoggedIn):
            print("Creating new user ")
            orderProcessorObj.create_user(conn)
            isUserLoggedIn = True
        
        while(isUserLoggedIn):
            print("\n1 to create user")
            print("2 to create product")
            print("3 to place order")
            print("4 to cancel order")
            print("5 to get all products")
            print("6 to get orders by user")
            print("7 to exit\n")

            choice = int(input("Enter your choice: "))
            if(choice == 7):
                # conn.close()
                break
            elif(choice == 1):
                orderProcessorObj.create_user(conn)
            elif(choice == 2):
                orderProcessorObj.create_product(conn)
            elif(choice == 3):
                orderProcessorObj.create_order(conn)
            elif(choice == 4):
                orderProcessorObj.cancel_order(conn)
            elif(choice == 5):
                list = orderProcessorObj.get_all_products(conn)
                for tuples in list:
                    print(f"Product Id : {tuples[0]}, ProductName : {tuples[1]}, Description : {tuples[2]}, Price : {tuples[3]}, QuantityInStock : {tuples[4]}, Type: {tuples[5]}")
            elif(choice == 6):
                # print(orderProcessorObj.get_order_by_user(conn))
                list = orderProcessorObj.get_order_by_user(conn)
                if(list == None):
                    print("No record")
                else:
                    for tuples in list:
                        print(f"OrderId : {tuples[0]}, UserId : {tuples[1]}, ProductId : {tuples[2]}")
                

        
MainModule.menu()
    
