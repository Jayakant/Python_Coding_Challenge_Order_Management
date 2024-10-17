import pyodbc
class DBConnUtil:
    @staticmethod
    def getConnObj(connStr):
        conn = pyodbc.connect(connStr)
        return conn

    