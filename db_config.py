import mysql.connector
from mysql.connector import Error
from datetime import datetime

class DatabaseConfig:
    def __init__(self):
        self.config = {
            'host': 'localhost',
            'user': 'root',
            'password': '',
            'database': 'membership_db'
        }
        # Test connection
        self.test_connection()
    
    def test_connection(self):
        try:
            connection = mysql.connector.connect(**self.config)
            if connection.is_connected():
                db_info = connection.get_server_info()
                print("\n=== Database Connection Status ===")
                print(f"Connected to MySQL Server version {db_info}")
                cursor = connection.cursor()
                cursor.execute("select database();")
                db_name = cursor.fetchone()[0]
                print(f"Connected to database: {db_name}")
                print("=================================\n")
                cursor.close()
                connection.close()
        except Error as e:
            print("\n=== Database Connection Error ===")
            print(f"Failed to connect to MySQL: {e}")
            print("================================\n")
            raise Exception("Database connection failed")

    def get_connection(self):
        try:
            connection = mysql.connector.connect(**self.config)
            return connection
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            return None

    def execute_query(self, query, params=None):
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                
                if query.strip().upper().startswith(('INSERT', 'UPDATE', 'DELETE')):
                    connection.commit()
                    return cursor.lastrowid
                else:
                    return cursor.fetchall()
            except Error as e:
                print(f"Error executing query: {e}")
                return None
            finally:
                cursor.close()
                connection.close()
        return None