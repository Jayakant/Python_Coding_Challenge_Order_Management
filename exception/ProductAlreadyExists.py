class ProductAlreadyExists(Exception):
    def __init__(self, message="Product already exists."):
        self.message = message
        super().__init__(self.message)
