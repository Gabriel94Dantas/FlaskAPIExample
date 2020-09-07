import sqlite3
from app.produce.producer import SqliteFactoryConnection


class Vessel:

    code = None
    sqlite_factory = SqliteFactoryConnection()

    def create_table(self):
        connection = None
        try:
            connection = self.sqlite_factory.get_connection()
            create_table_query = '''CREATE TABLE vessel (
                                    code  TEXT
                                    );'''
            cursor = connection.cursor()
            cursor.execute(create_table_query)
            connection.commit()
            self.sqlite_factory.close_cursor(cursor)

        except sqlite3.Error as error:
            print("Error while creating a sqlite table", error)
        finally:
            if connection:
                self.sqlite_factory.close_connection(connection)

    def insert(self, vessel):
        connection = None
        try:
            connection = self.sqlite_factory.get_connection()
            insert_query = '''INSERT INTO vessel (code) 
                            VALUES(?)
                            '''
            data_tuple = (str(vessel.code),)
            cursor = connection.cursor()
            cursor.execute(insert_query, data_tuple)
            connection.commit()
            self.sqlite_factory.close_cursor(cursor)
        except sqlite3.Error as error:
            print("Error while inserting a sqlite register", error)
        finally:
            if connection:
                self.sqlite_factory.close_connection(connection)

    def select_vessel_by_code(self, code):
        connection = None
        try:
            connection = self.sqlite_factory.get_connection()
            select_query = '''SELECT code from vessel where code = ? '''
            data_tuple = (str(code),)
            cursor = connection.cursor()
            cursor.execute(select_query, data_tuple)
            returned_code = cursor.fetchone()
            self.sqlite_factory.close_cursor(cursor)

            return returned_code
        except sqlite3.Error as error:
            print("Error while selecting a sqlite tuple", error)
        finally:
            if connection:
                self.sqlite_factory.close_connection(connection)

    def delete_all(self):
        connection = None
        try:
            connection = self.sqlite_factory.get_connection()
            select_query = '''DELETE FROM vessel '''
            cursor = connection.cursor()
            cursor.execute(select_query)
            connection.commit()
            self.sqlite_factory.close_cursor(cursor)

        except sqlite3.Error as error:
            print("Error while selecting a sqlite tuple", error)
        finally:
            if connection:
                self.sqlite_factory.close_connection(connection)