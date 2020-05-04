import sqlite3
from tabulate import tabulate


def add_new_repair_hour():
    new_date = input('Repair hour date: ')
    new_hour = input('Start Hour: ')
    connection = sqlite3.connect('vehicle_repair_manager.db')
    cursor = connection.cursor()
    add_repair_hour = '''
        INSERT INTO RepairHour(data, start_hour)
          VALUES (?, ?)
        '''
    cursor.execute(add_repair_hour, (new_date, new_hour))
    connection.commit()

    all_repair_hour = '''
        SELECT id, data, start_hour
          FROM RepairHour
          WHERE vehicle IS NULL
        '''
    cursor.execute(all_repair_hour)
    connection.commit()
    hours = cursor.fetchall()
    print(tabulate([hour for hour in hours], headers=['id', 'data', 'start_hour']))
    connection.close()


def add_new_service():
    new_service = input('Provide New service name: ')
    connection = sqlite3.connect('vehicle_repair_manager.db')
    cursor = connection.cursor()
    add_service = '''
        INSERT INTO Service(name)
          VALUES (?)
        '''
    cursor.execute(add_service, (new_service, ))
    connection.commit()
    connection.close()
    print('You add new service successfully!')
