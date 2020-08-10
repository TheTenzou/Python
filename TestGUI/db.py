import mysql.connector
import mysql.connector.pooling
import mysql.connector.optionfiles


class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="Admin",
            passwd="adminpas1337",
            database="part_manager")

        self.cursor = self.connection.cursor()
        self.cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS 
        parts ( id INTEGER PRIMARY KEY,
                part varchar(500), 
                customer varchar(200),
                retailer varchar(300),
                price varchar(100))''')
        self.connection.commit()

    def fetch(self):
        self.cursor.execute("SELECT * FROM parts")
        rows = self.cursor.fetchall()
        return rows

    def insert(self, part, customer, retailer, price):
        self.cursor.execute(
            'INSERT INTO parts VALUES (NULL, \'' + part + '\', \'' + customer + '\', \'' + retailer + '\', \'' + price + '\')')
        self.connection.commit()

    def remove(self, id_):
        self.cursor.execute("DELETE FROM parts WHERE id = " + str(id_, ))
        self.connection.commit()

    def update(self, id, part, customer, retailer, price):
        self.cursor.execute('''
        UPDATE parts SET 
            part = \'''' + part + '''\',
            customer = \'''' + customer + '''\',
            retailer = \'''' + retailer + '''\',
            price = \'''' + price + '''\'
        WHERE
            id = \'''' + str(id) + '''\'
            ''')
        self.connection.commit()

    def __del__(self):
        self.connection.close()
