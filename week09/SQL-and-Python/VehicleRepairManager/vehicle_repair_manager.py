import sqlite3
from tabulate import tabulate
import random


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


def user_id(*, user_name):
    connection = sqlite3.connect('vehicle_repair_manager.db')
    cursor = connection.cursor()
    the_user_id = '''
        SELECT id
          FROM BaseUser
          WHERE user_name=(?)
        '''
    cursor.execute(the_user_id, (user_name, ))
    connection.commit()
    user = cursor.fetchone()
    connection.close()
    return user[0]


def add_new_client(*, user_name, phone_number, email, address):
    connection = sqlite3.connect('vehicle_repair_manager.db')
    cursor = connection.cursor()
    add_into_base_user = '''
        INSERT INTO BaseUser(user_name, phone_number, email, address) VALUES(?, ?, ?, ?)
        '''
    cursor.execute(add_into_base_user, (user_name, phone_number, email, address))
    connection.commit()

    user = user_id(user_name=user_name)

    add_into_client = '''
        INSERT INTO Client(base_id) VALUES(?)
        '''
    cursor.execute(add_into_client, (user, ))
    connection.commit()
    connection.close()


def add_new_mechanic(*, user_name, phone_number, email, address, title):
    connection = sqlite3.connect('vehicle_repair_manager.db')
    cursor = connection.cursor()
    add_into_base_user = '''
        INSERT INTO BaseUser(user_name, phone_number, email, address) VALUES(?, ?, ?, ?)
        '''
    cursor.execute(add_into_base_user, (user_name, phone_number, email, address))
    connection.commit()

    user = user_id(user_name=user_name)

    add_into_mechanic = '''
        INSERT INTO Mechanic(base_id, title) VALUES(?, ?)
        '''
    cursor.execute(add_into_mechanic, (user, title))
    connection.commit()
    connection.close()


def list_all_free_hours():
    connection = sqlite3.connect('vehicle_repair_manager.db')
    cursor = connection.cursor()
    all_hours = '''
        SELECT id, data, start_hour
          FROM RepairHour
          WHERE vehicle IS NULL
        '''
    cursor.execute(all_hours)
    connection.commit()
    datas = cursor.fetchall()
    print(tabulate([x for x in datas], headers=['id', 'data', 'start_hour']))

    connection.close()


def list_free_hours(*, data):
    connection = sqlite3.connect('vehicle_repair_manager.db')
    cursor = connection.cursor()
    all_hours = '''
        SELECT id, data, start_hour
          FROM RepairHour
          WHERE data LIKE (?)
        '''
    cursor.execute(all_hours, (data, ))
    connection.commit()
    datas = cursor.fetchall()
    print(tabulate([x for x in datas], headers=['id', 'data', 'start_hour']))

    connection.close()


def add_vehicle(*, user_name):
    category = input('Vehicle category: ')
    make = input('Vehicle make: ')
    model = input('Vehicle model: ')
    register_number = input('Vehicle register number: ')
    gear_box = input('Vehicle gear box: ')

    connection = sqlite3.connect('vehicle_repair_manager.db')
    cursor = connection.cursor()
    new_vehicle = '''
        INSERT INTO Vehicle(category, make, model, register_number, gear_box, owner)
          VALUES(?, ?, ?, ?, ?, ?)
        '''
    client = user_id(user_name=user_name)
    cursor.execute(new_vehicle, (category, make, model, register_number, gear_box, client))
    connection.commit()
    connection.close()

    print('Thank you! You added new personal vehicle!')


def save_repair_hour(*, hour_id):
    print('Choose vehicle to repair: ')
    connection = sqlite3.connect('vehicle_repair_manager.db')
    cursor = connection.cursor()
    all_vehicles = '''
        SELECT *
          FROM Vehicle
        '''

    cursor.execute(all_vehicles)
    connection.commit()
    vehicles = cursor.fetchall()

    ids = [x[0] for x in vehicles]
    all_v = []

    for x in vehicles:
        vehicle = ''
        for i in range(2, 5):
            vehicle += ''.join(x[i] + ' ')
            if i == 3:
                vehicle += ''.join(' with RegNumber: ')

        all_v.append(vehicle)

    print(tabulate({'id': [el for el in ids], 'Vehicle': [el for el in all_v]}, headers='keys'))

    choosen_vehicle = input('>>: ')

    id_vehicle = '''
        SELECT *
          FROM Vehicle
          WHERE id = (?)
        '''

    cursor.execute(id_vehicle, (choosen_vehicle, ))
    connection.commit()

    vehicle_fk = cursor.fetchone()

    print('Choose service: ')
    all_services = '''
        SELECT *
          FROM Service
        '''
    cursor.execute(all_services)
    connection.commit()

    services = cursor.fetchall()

    print(tabulate([service for service in services], headers=['id', 'Service']))

    choosen_service = input('>>: ')

    id_mechanic_service = '''
        SELECT *
          FROM MechanicService
          WHERE service_id = (?)
        '''
    cursor.execute(id_mechanic_service, (choosen_service, ))
    connection.commit()

    mechanic_service = cursor.fetchone()

    update_repair_hour = '''
        UPDATE RepairHour
          SET vehicle = (?),
              bill = (?),
              mechanic_service = (?)
          WHERE id = (?)
        '''
    bill = random.uniform(50, 1000)
    cursor.execute(update_repair_hour, (vehicle_fk[0], bill, mechanic_service[0], hour_id))
    cursor.execute('''SELECT * FROM RepairHour WHERE id =(?)''', (hour_id, ))
    info = cursor.fetchone()

    cursor.execute('''SELECT * FROM Service WHERE id =(?)''', (mechanic_service[2], ))
    info_service = cursor.fetchone()

    connection.commit()
    connection.close()

    print(f'''Thank you! You saved an hour on {info[1]}, at {info[2]} for {info_service[1]}!
        Vehicle: {vehicle_fk[2]} {vehicle_fk[3]} with RegNumber: {vehicle_fk[4]}.''')


def delete_repair_hour(*, hour_id):
    connection = sqlite3.connect('vehicle_repair_manager.db')
    cursor = connection.cursor()
    delete_hour = '''
        UPDATE RepairHour
          SET vehicle = NULL,
              bill = NULL,
              mechanic_service = NULL
          WHERE id = (?)
        '''
    cursor.execute(delete_hour, (hour_id))
    print('You delete the repaired hour successfully!')
    connection.commit()
    connection.close()


def update_repair_hour(*, hour_id):
    new_data = input('Enter new data: ')
    new_hour = input('Enter new hour: ')
    connection = sqlite3.connect('vehicle_repair_manager.db')
    cursor = connection.cursor()
    update_data = '''
        UPDATE RepairHour
          SET data = (?),
              start_hour = (?)
          WHERE id = (?)
        '''
    cursor.execute(update_data, (new_data, new_hour, hour_id))
    connection.commit()
    connection.close()
    print('You update the repaired hour successfully!')


def list_personal_vehicles(*, user_name):
    connection = sqlite3.connect('vehicle_repair_manager.db')
    cursor = connection.cursor()
    all_vehicles = '''
        SELECT *
          FROM Vehicle
          WHERE owner = (?)
        '''
    owner = user_id(user_name=user_name)
    cursor.execute(all_vehicles, (owner, ))
    connection.commit()
    vehicles = cursor.fetchall()
    print(tabulate([x for x in vehicles], headers=['id', 'Category', 'Make', 'Model', 'Register Number', 'Gear Box', 'OwnerId']))


def update_vehicle(*, vehicle_id):
    connection = sqlite3.connect('vehicle_repair_manager.db')
    cursor = connection.cursor()
    print('What do you want to update? ')
    new_category = input('New category: ')
    new_make = input('New made: ')
    new_model = input('New model: ')
    new_reg_num = input('New register number: ')
    new_gear_box = input('New gear box: ')
    new_owner = input('New owner id: ')
    cursor.execute('''SELECT * FROM Vehicle WHERE id = (?)''', (vehicle_id, ))
    new_data = []

    vehicle_info = cursor.fetchone()

    if new_category != '':
        new_data.append(new_category)
    else:
        new_category = vehicle_info[1]
        new_data.append(new_category)

    if new_make != '':
        new_data.append(new_make)
    else:
        new_make = vehicle_info[2]
        new_data.append(new_make)

    if new_model != '':
        new_data.append(new_model)
    else:
        new_model = vehicle_info[3]
        new_data.append(new_model)

    if new_reg_num != '':
        new_data.append(new_reg_num)
    else:
        new_reg_num = vehicle_info[4]
        new_data.append(new_reg_num)

    if new_gear_box != '':
        new_data.append(new_gear_box)
    else:
        new_gear_box = vehicle_info[5]
        new_data.append(new_gear_box)

    if new_owner != '':
        new_owner_id = user_id(user_name=new_owner)
        new_data.append(new_owner_id)
    else:
        new_owner = vehicle_info[6]
        new_data.append(new_owner)

    new_data.append(vehicle_id)
    update_data = '''
        UPDATE Vehicle
          SET category = (?),
              make = (?),
              model = (?),
              register_number = (?),
              gear_box = (?),
              owner = (?)
          WHERE id = (?)
        '''
    cursor.execute(update_data, tuple(new_data))
    connection.commit()
    connection.close()
    print('You update the vehicle successfully!')


def delete_vehicle(*, vehicle_id):
    connection = sqlite3.connect('vehicle_repair_manager.db')
    cursor = connection.cursor()
    cursor.execute('''DELETE FROM Vehicle WHERE id = (?)''', (vehicle_id, ))
    connection.commit()
    connection.close()
    print('You delete the vehicle successfully!')


def output_for_new_client(*, user_name):
    print(f'''
    Thank you, {user_name}!
    Welcome to Vehicle Services!
    Next time you try to login, provide your user_name!
        ''')


def print_menu():
    print('''
    You can choose from the following commands:
    list_all_free_hours
    list_free_hours <date>
    save_repair_hour <hour_id>
    update_repair_hour <hour_id>
    delete_repair_hour <hour_id>
    list_personal_vehicles
    add_vehicle
    update_vehicle <vehicle_id>
    delete_vehicle <vehicle_id>
    exit
        ''')


def menu_for_client(*, user_name):
    exit = False
    print_menu()

    while exit is not True:
        command = input('command: ')
        if command == 'list_all_free_hours':
            list_all_free_hours()
        elif 'list_free_hours' in command:
            list_free_hours(data=command.split(' ')[-1])
        elif 'save_repair_hour' in command:
            save_repair_hour(hour_id=command.split(' ')[-1])
        elif 'update_repair_hour' in command:
            update_repair_hour(hour_id=command.split(' ')[-1])
        elif 'delete_repair_hour' in command:
            delete_repair_hour(hour_id=command.split(' ')[-1])
        elif command == 'add_vehicle':
            add_vehicle(user_name=user_name)
        elif command == 'list_personal_vehicles':
            list_personal_vehicles(user_name=user_name)
        elif 'update_vehicle' in command:
            update_vehicle(vehicle_id=command.split(' ')[-1])
        elif 'delete_vehicle' in command:
            delete_vehicle(vehicle_id=command.split(' ')[-1])
        elif command == 'exit':
            exit = True


def checking_by_user_name(*, user_name):
    connection = sqlite3.connect('vehicle_repair_manager.db')
    cursor = connection.cursor()
    search = '''
        SELECT *
          FROM BaseUser
          WHERE user_name = (?)
        '''
    cursor.execute(search, (user_name, ))
    user = cursor.fetchall()
    if len(user) == 0:
        print('Unknown user!')
        new_user = input('Would you like to create new user? ')
        if new_user in ['yes', 'y']:
            type_user = input('Are you a Client or Mechanic? ')
            name = input('Provide user_name: ')
            phone_number = input('Provide phone_number: ')
            email = input('Provide email: ')
            address = input('Provide address: ')
            if type_user.lower() == 'client':
                add_new_client(user_name=name, phone_number=phone_number, email=email, address=address)
                output_for_new_client(user_name=name)
                menu_for_client(user_name=user_name)
            else:
                title = input('Enter your title: ')
                add_new_mechanic(user_name=name, phone_number=phone_number, email=email, address=address, title=title)
                output_for_new_client(user_name=name)
                # menu(user_name=user_name)
    else:
        print(f'Hello, {user_name}!')
        menu_for_client(user_name=user_name)


def main():
    create_tables()
    print('Hello!')
    user_name = input('Provide user name: ')
    checking_by_user_name(user_name=user_name)


if __name__ == '__main__':
    main()
