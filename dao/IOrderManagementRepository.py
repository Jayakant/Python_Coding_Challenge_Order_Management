from abc import ABC, abstractmethod
# from entity.User import User
# from entity.Product import Product

class IOrderManagementRepository(ABC):
    @abstractmethod
    def create_order(self, conn):
        pass

    @abstractmethod
    def cancel_order(self, conn):
        pass

    @abstractmethod
    def create_product(self, conn):
        pass

    @abstractmethod
    def create_user(self, conn):
        pass

    @abstractmethod
    def get_all_products(self,conn):
        pass

    @abstractmethod
    def get_order_by_user(self, conn):
        pass
