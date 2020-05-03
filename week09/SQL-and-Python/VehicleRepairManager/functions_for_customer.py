import sqlite3
from tabulate import tabulate
import random
from utils import user_id


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
