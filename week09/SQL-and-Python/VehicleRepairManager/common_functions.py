import sqlite3
from tabulate import tabulate


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
