class OrderAlreadyExists(Exception):
    def __init__(self, message="Order already exists."):
        self.message = message
        super().__init__(self.message)
