import sqlite3


def create_tables():
    connection = sqlite3.connect('vehicle_repair_manager.db')
    cursor = connection.cursor()
    base_user = '''
        CREATE TABLE IF NOT EXISTS BaseUser (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          user_name VARCHAR(20),
          email VARCHAR(20),
          phone_number VARCHAR(20),
          address VARCHAR(30)
        )
        '''
    client = '''
        CREATE TABLE IF NOT EXISTS Client (
          base_id INTEGER,
          FOREIGN KEY(base_id) REFERENCES BaseUser(id)
        )
        '''
    mechanic = '''
        CREATE TABLE IF NOT EXISTS Mechanic (
          base_id INTEGER,
          title VARCHAR(30),
          FOREIGN KEY(base_id) REFERENCES BaseUser(id)
        )
        '''
    service = '''
        CREATE TABLE IF NOT EXISTS Service(
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          name VARCHAR(20)
        )
        '''
    mechanic_service = '''
        CREATE TABLE IF NOT EXISTS MechanicService(
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          mechanic_id INTEGER,
          service_id INTEGER,
          FOREIGN KEY(mechanic_id) REFERENCES Mechanic(base_id)
          FOREIGN KEY(service_id) REFERENCES Service(id)
        )
        '''
    vehicle = '''
        CREATE TABLE IF NOT EXISTS Vehicle (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          category VARCHAR (20),
          make VARCHAR(20),
          model VARCHAR(20),
          register_number VARCHAR(20),
          gear_box VARCHAR(20),
          owner INTEGER,
          FOREIGN KEY(owner) REFERENCES Client(base_id)
        )
        '''
    repair_hour = '''
        CREATE TABLE IF NOT EXISTS RepairHour (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          data VARCHAR(20),
          start_hour VARCHAR(20),
          vehicle INTEGER,
          bill REAL,
          mechanic_service INTEGER,
          FOREIGN KEY(vehicle) REFERENCES Vehicle(id)
          FOREIGN KEY(mechanic_service) REFERENCES MechanicService(id)
        )
        '''
    cursor.execute(base_user)
    cursor.execute(client)
    cursor.execute(mechanic)
    cursor.execute(service)
    cursor.execute(mechanic_service)
    cursor.execute(vehicle)
    cursor.execute(repair_hour)

    connection.commit()
    connection.close()
