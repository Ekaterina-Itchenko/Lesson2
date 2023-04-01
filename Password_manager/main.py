from validation import check_choice
from errors import NotDigitError, UnexpectedNumberError
from providers import key_provider, password_provider, export_provider
from config import KEY_STORAGE, CODE_STORAGE, PASSWORD_STORAGE
from busines_logic import PasswordManager


while True:
    choice = input('Choose the action from menu:\n'
                   '1 - Add new password\n'
                   '2 - Get list of password identifiers\n'
                   '3 - Get a specific password\n'
                   '4 - Remove selected password\n'
                   '5 - Export all passwords\n'
                   '6 - Exit\n'
                   'Your choice: '
                   )
    try:
        check_choice(choice)
    except NotDigitError as err:
        print(err)
        continue
    except UnexpectedNumberError as err:
        print(err)
        continue

    key_connector = key_provider(CODE_STORAGE, KEY_STORAGE)
    if not key_connector.validate_key_existence():
        key = key_connector.generate_key()
        print(f'Remember this code phrase: {key}')

    pm = PasswordManager(password_provider(PASSWORD_STORAGE))

    if int(choice) == 1:
        identifier = input("Enter password identifier: ")
        password = input("Enter a password: ")
        entered_key = input("Enter a code phrase: ")
        try:
            key_connector.validate_key(entered_key)
            pm.add_password(password,
                            identifier,
                            entered_key)
        except ValueError as err:
            print(err)
            continue

    elif int(choice) == 2:
        print(pm.get_password_list())

    elif int(choice) == 3:
        identifier = input("Enter password identifier: ")
        entered_key = input("Enter a code phrase: ")
        try:
            key_connector.validate_key(entered_key)
            print(pm.get_password(identifier,
                                  entered_key))
        except ValueError as err:
            print(err)
            continue

    elif int(choice) == 4:
        identifier = input("Enter password identifier: ")
        entered_key = input("Enter a code phrase: ")
        try:
            key_connector.validate_key(entered_key)
            pm.delete(identifier)
        except ValueError as err:
            print(err)
            continue

    elif int(choice) == 5:
        entered_key = input("Enter a code phrase: ")
        file_name = input("Enter a a file name to export: ")
        try:
            key_connector.validate_key(entered_key)
            pm.export_all_passwords(export_provider(file_name),
                                    entered_key)
        except ValueError as err:
            print(err)
            continue

    elif int(choice) == 6:
        print('GOODBYE')
        break
