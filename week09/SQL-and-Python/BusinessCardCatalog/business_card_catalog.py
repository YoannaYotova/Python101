import sqlite3

def pritnting(contact):
    print('\n###############\n')
    print('Id: ', contact[0])
    print('Full name: ', contact[1])
    print('Email: ', contact[2])
    print('Age: ', contact[3])
    print('Phone: ', contact[4])
    print('Additional contact: ', contact[5])
    print('\n###############\n')

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

def list():
    print('''
        #############
        ###Contacts###
        #############
        ''')
    connection = sqlite3.connect('business_card_catalog.db')
    cursor = connection.cursor()
    all_contacts = '''
        SELECT * FROM users
        '''
    cursor.execute(all_contacts)
    contacts = cursor.fetchall()
    for contact in contacts:
        print(f'ID:  {contact[0]},  Email: {contact[2]},  Full name:  {contact[1]}')

    connection.close()


def get():
    contact_id = int(input('Enter id: '))
    print('Contact info:')
    connection = sqlite3.connect('business_card_catalog.db')
    cursor = connection.cursor()
    contact = '''
        SELECT * FROM users WHERE id = (?)
        '''
    cursor.execute(contact, (contact_id, ))
    contact = cursor.fetchone()
    pritnting(contact)

    connection.close()


def delete():
    contact_id = int(input('Enter id: '))
    connection = sqlite3.connect('business_card_catalog.db')
    cursor = connection.cursor()
    contact = '''
        SELECT * FROM users WHERE id = (?)
        '''
    cursor.execute(contact, (contact_id, ))
    contact = cursor.fetchone()
    deleting = '''
        DELETE FROM users WHERE id = (?)
        '''
    cursor.execute(deleting, (contact_id, ))
    connection.commit()
    print('Following contact is deleted successfully: ')
    pritnting(contact)

    connection.close()  


def main():
    create_database()
    print('''
        Hello! This is your business card catalog.
        What would you like? (enter "help" to list all available options)
        ''')
    while True:
        command = input('Enter command: ')
        if command == 'add':
            add()
        elif command == 'help':
            help()
        elif command == 'list':
            list()
        elif command == 'get':
            get()
        elif command == 'delete':
            delete()
        else:
            break


if __name__ == '__main__':
    main()
