import mysql.connector
from mysql.connector import Error

class Mydb:
    "database user password"

    def __init__(self, db_name):
    #def __init__(self):
        self.db_name = db_name
        self.db_user = 'oleg'
        self.db_pass = 'hs,fkrf'
        self.conn = ''
        self.connect()
        
    def connect(self):
        """ Connect to MySQL database """
        try:
            self.conn = mysql.connector.connect(host='localhost',
                                           database=self.db_name,
                                           user=self.db_user,
                                           password=self.db_pass)
            if self.conn.is_connected():
                print('Connected to MySQL database ' + self.db_name)

        except Error as e:
            print(e)

    def fetch(self, query):
        self.rows = []
        cursor = self.conn.cursor()
        cursor.execute(query)
        row = cursor.fetchone()

        while row is not None:
            self.rows.append(row)
            row = cursor.fetchone()

        return self.rows

    def query(self, query):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            print cursor

            if cursor.lastrowid:
                print('last insert id', cursor.lastrowid)
            else:
                print('last insert id not found')

            self.conn.commit()
        except Error as error:
            print(error)

    def __del__(self):
        self.conn.close()

