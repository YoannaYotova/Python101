import sqlite3


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
