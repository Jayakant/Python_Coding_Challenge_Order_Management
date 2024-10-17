from .Product import Product

class Clothing(Product):
    def __init__(self, ProductId, productName, description, price, quantityInStock, size, color):
        super().__init__(ProductId, productName, description, price, quantityInStock, "Clothing")
        self.size = size
        self.color = color
