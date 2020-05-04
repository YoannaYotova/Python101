import sqlite3
from utils import print_menu_client, print_menu_mechanic, output_for_new_client, user_id, in_database
from create_tables import create_tables
from functions_for_customer import (save_repair_hour,
                                    delete_repair_hour,
                                    update_vehicle, delete_vehicle,
                                    add_vehicle, list_personal_vehicles)
from common_functions import list_free_hours, list_all_free_hours, update_repair_hour


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


def menu_for_client(*, user_name):
    exit = False
    print_menu_client(user_name=user_name)

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


def menu_for_mechanic(*, user_name):
    # exit = False
    print_menu_mechanic(user_name=user_name)


def login(*, username):
    if not in_database(table='BaseUser', user_name=username):
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
                menu_for_client(user_name=username)
            elif type_user.lower() == 'mechanic':
                title = input('Enter your title: ')
                add_new_mechanic(user_name=name, phone_number=phone_number, email=email, address=address, title=title)
                output_for_new_client(user_name=name)
                # menu(user_name=user_name)
    else:
        customer_id = user_id(user_name=username)
        if in_database(table='Client', base_id=customer_id):
            menu_for_client(user_name=username)
        elif in_database(table='Mechanic', base_id=customer_id):
            menu_for_mechanic(user_name=username)


def main():
    create_tables()
    print('Hello!')
    user_name = input('Provide user name: ')
    login(username=user_name)


if __name__ == '__main__':
    main()
