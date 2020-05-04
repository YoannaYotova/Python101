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
    cursor.execute(all_hours, ('%' + data + '%', ))
    connection.commit()
    datas = cursor.fetchall()
    print(datas)
    print(tabulate([x for x in datas], headers=['id', 'data', 'start_hour']))

    connection.close()
