import mysql.connector
import os

class MySQLDB:
    def __init__(self, host, user, pasword, database):
        self.host = host
        self.user = user
        self.pw = pasword
        self.db = database

        def connect(self):
            try:
                if(self.connection == None):
                    self.connection = mysql.connector.connect(
                        host = self.host, 
                        user = self.user, 
                        pasword = self.pw,
                        database = slice.db,
                        )
                    os.system("color a2")
                    print("wow, me conecte satisfactoriamente")

            except mysql.connector.Error as error:
                print("Error mientras se estaba conectando {}".format(error))    

    def disconnect(self):
        try:
            if self.connection:
                self.connection.close
                self.connection = None
        except mysql.connector.Error as error:
            print("Error")   

    def execute_query(self, query, params=None):
        try:
            cursor = self.connection.cursor() 
            cursor .execute(query, params)
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            print(f"Error: {err}")



db = MySQLDB("localhost", "root", "", "testlp")