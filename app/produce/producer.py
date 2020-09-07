import sqlite3

class SqliteFactoryConnection():

    def get_connection(self):
        return sqlite3.connect('FlaskAPIExample.db')

    def close_cursor(self, cursor):
        cursor.close()

    def close_connection(self, connection):
        connection.close()
