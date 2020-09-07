from app.produce.producer import SqliteFactoryConnection
from app.entity.vessel import Vessel
import sqlite3


class Equipment:
    name = None
    code = None
    vessel = None
    location = None
    status = None
    sqliteFactory = SqliteFactoryConnection()

    def create_table(self):
        connection = None
        try:
            connection = self.sqliteFactory.get_connection()
            create_table_query = ''' CREATE TABLE equipment(
                                name TEXT,
                                code TEXT,
                                vessel_code TEXT,
                                location TEXT,
                                status BOOLEAN    
                                ); '''
            cursor = connection.cursor()
            cursor.execute(create_table_query)
            connection.commit()
            self.sqliteFactory.close_cursor(cursor)

        except sqlite3.Error as error:
            print("Error while creating a sqlite table", error)
        finally:
            if connection:
                self.sqliteFactory.close_connection(connection)

    def insert(self, equipment):
        connection = None
        try:
            connection = self.sqliteFactory.get_connection()
            insert_query = '''INSERT INTO equipment (
                            name, code, vessel_code, location, status
                            ) VALUES(?,?,?,?,?)'''
            data_tuple = (equipment.name,
                          equipment.code,
                          equipment.vessel.code,
                          equipment.location,
                          equipment.status,
                          )
            cursor = connection.cursor()
            cursor.execute(insert_query, data_tuple)
            connection.commit()
            self.sqliteFactory.close_cursor(cursor)

        except sqlite3.Error as error:
            print("Error while inserting a sqlite register", error)
        finally:
            if connection:
                self.sqliteFactory.close_connection(connection)

    def update(self, status, code):
        connection = None
        try:
            connection = self.sqliteFactory.get_connection()
            update_query = '''UPDATE equipment SET status = ? WHERE code = ?'''
            data_tuple = (status, str(code),)
            cursor = connection.cursor()
            cursor.execute(update_query, data_tuple)
            connection.commit()
            self.sqliteFactory.close_cursor(cursor)
        except sqlite3.Error as error:
            print("Error while updating a sqlite register", error)
        finally:
            if connection:
                self.sqliteFactory.close_connection(connection)

    def select_active_equipment_of_vessel(self, vessel_code):
        connection = None
        try:
            connection = self.sqliteFactory.get_connection()
            select_query = '''SELECT name, code, vessel_code, location, status 
                                FROM equipment WHERE status = 1 
                                AND vessel_code = ?
                            '''
            data_tuple = (str(vessel_code),)
            cursor = connection.cursor()
            cursor.execute(select_query, data_tuple)
            rows = cursor.fetchall()
            equipments = []
            for row in rows:
                equipment = Equipment()
                vessel = Vessel()
                equipment.name = row[0]
                equipment.code = row[1]
                vessel.code = row[2]
                equipment.vessel = vessel
                equipment.location = row[3]
                equipment.status = row[4]
                equipments.append(equipment)
            self.sqliteFactory.close_cursor(cursor)
            return equipments
        except sqlite3.Error as error:
            print("Error while selecting a sqlite register", error)
        finally:
            self.sqliteFactory.close_connection(connection)

    def delete_all(self):
        connection = None
        try:
            connection = self.sqliteFactory.get_connection()
            select_query = '''DELETE FROM equipment '''
            cursor = connection.cursor()
            cursor.execute(select_query)
            connection.commit()
            self.sqliteFactory.close_cursor(cursor)

        except sqlite3.Error as error:
            print("Error while selecting a sqlite tuple", error)
        finally:
            if connection:
                self.sqliteFactory.close_connection(connection)
