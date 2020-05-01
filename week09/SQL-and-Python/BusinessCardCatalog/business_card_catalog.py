import sqlite3


def create_database():
    connection = sqlite3.connect('business_card_catalog.db')
    cursor = connection.cursor()
    table = '''
        CREATE TABLE IF NOT EXISTS users(
          id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
          full_name VARCHAR(100) NOT NULL UNIQUE,
          email VARCHAR(100) UNIQUE,
          age INTEGER NOT NULL,
          phone VARCHAR(20) NOT NULL,
          additional_info TEXT
        )
    '''

    cursor.execute(table)
    connection.commit()
    connection.close()


def help():
    print('''
        #############
        ###Options###
        #############
        ''')
    print('''
        1. `add` - insert new business card
        2. `list` - list all business cards
        3. `delete` - delete a certain business card (`ID` is required)
        4. `get` - display full information for a certain business card (`ID` is required)
        5. `help` - list all available options
        ''')


def add():
    connection = sqlite3.connect('business_card_catalog.db')
    cursor = connection.cursor()
    full_name = input('Enter user name: ')
    email = input('Enter email: ')
    age = input('Enter age: ')
    phone = input('Enter phone: ')
    additional_info = input('Enter additional_info (optional): ')
    insert_info = '''
        INSERT INTO users (full_name, email, age, phone, additional_info)
          VALUES(?, ?, ?, ?, ?)
    '''
    if additional_info == '':
        additional_info = None

    cursor.execute(insert_info, (full_name, email, age, phone, additional_info))

    connection.commit()
    connection.close()


def main():
    create_database()
    print('''Hello! This is your business card catalog.\
        What would you like? (enter "help" to list all available options)''')
    while True:
        command = input('Enter command: ')
        if command == 'add':
            add()
        elif command == 'help':
            help()


if __name__ == '__main__':
    main()
