import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from CRUD_business_logic import ( # noqa E402
    BooksService,
    AuthorsService,
    TransactionsService,
    UserService,
    InvalidIdError
) # noqa E402
from CRUD_presentation_layer.validation import validate_choice, validate_id # noqa E402
from CRUD_presentation_layer.exeptions import InvalidChoice, NotDigitError # noqa E402
from data_access import SqliteConnector # noqa E402
from CRUD_presentation_layer.db_providers import db_provider # noqa E402
from CRUD_presentation_layer.config import DB_NAME, DB_TYPE # noqa E402


while True:
    choice = input('1 - users;\n'
                   '2 - books;\n'
                   '3 - authors;\n'
                   '4 - transactions;\n'
                   '5 - exit\n'
                   'Your choice: ')
    try:
        validate_choice(choice=choice, start=1, stop=5)
    except InvalidChoice as err:
        print(err)
        continue
    connector = SqliteConnector(db_name='book_st.db')

    if int(choice) == 1:
        inner_choice = input('1 - List of all users\n'
                             '2 - Get user info\n'
                             '3 - Delete user\n'
                             '4 - Update user email\n'
                             '5 - Update user phone\n'
                             'Your choice: ')
        try:
            validate_choice(choice=inner_choice, start=1, stop=5)
        except InvalidChoice as err:
            print(err)
            continue

        if int(inner_choice) == 1:
            res = UserService(
                db_provider(DB_NAME, DB_TYPE)
            ).get_all_users_list()
            print(res)

        if int(inner_choice) == 2:
            user_id = input('Enter user id: ')

            try:
                validate_id(user_id)
                res = UserService(
                    db_connector=db_provider(DB_NAME, DB_TYPE)
                ).get_user_info(int(user_id))
                print(res)
            except NotDigitError as err:
                print(err)
                continue
            except InvalidIdError as err:
                print(err)
                continue

        if int(inner_choice) == 3:
            user_id = input('Enter user id: ')
            try:
                validate_id(user_id)
                UserService(
                    db_connector=db_provider(DB_NAME, DB_TYPE)
                ).delete_user(int(user_id))
            except NotDigitError as err:
                print(err)
                continue
            except InvalidIdError as err:
                print(err)
                continue

        if int(inner_choice) == 4:
            user_id = input('Enter user id: ')
            new_email = input('Enter new user email: ')
            try:
                validate_id(user_id)
                UserService(
                    db_connector=db_provider(DB_NAME, DB_TYPE)
                ).update_user_email(int(user_id), new_email=new_email)
            except NotDigitError as err:
                print(err)
                continue
            except InvalidIdError as err:
                print(err)
                continue

        if int(inner_choice) == 5:
            user_id = input('Enter user id: ')
            new_phone = input('Enter new user phone number: ')
            try:
                validate_id(user_id)
                UserService(
                    db_connector=db_provider(DB_NAME, DB_TYPE)
                ).update_user_phone(int(user_id), new_phone=new_phone)
            except NotDigitError as err:
                print(err)
                continue
            except InvalidIdError as err:
                print(err)
                continue

    if int(choice) == 2:
        inner_choice = input('1 - List of all books\n'
                             '2 - Get book info\n'
                             '3 - Delete book\n'
                             '4 - Update book Name\n'
                             'Your choice: ')
        try:
            validate_choice(choice=inner_choice, start=1, stop=4)
        except InvalidChoice as err:
            print(err)
            continue

        if int(inner_choice) == 1:
            res = BooksService(
                db_provider(DB_NAME, DB_TYPE)
            ).get_all_books_list()
            print(res)

        if int(inner_choice) == 2:
            book_id = input('Enter book id: ')

            try:
                validate_id(book_id)
                res = BooksService(
                    db_connector=db_provider(DB_NAME, DB_TYPE)
                ).get_book_info(int(book_id))
                print(res)
            except NotDigitError as err:
                print(err)
                continue
            except InvalidIdError as err:
                print(err)
                continue

        if int(inner_choice) == 3:
            book_id = input('Enter book id: ')

            try:
                validate_id(book_id)
                BooksService(
                    db_connector=db_provider(DB_NAME, DB_TYPE)
                ).delete_book(int(book_id))
            except NotDigitError as err:
                print(err)
                continue
            except InvalidIdError as err:
                print(err)
                continue

        if int(inner_choice) == 4:
            book_id = input('Enter book id: ')
            new_name = input('Enter new title of book: ')

            try:
                validate_id(book_id)
                BooksService(
                    db_connector=db_provider(DB_NAME, DB_TYPE)
                ).update_book_name(int(book_id), new_name)
            except NotDigitError as err:
                print(err)
                continue
            except InvalidIdError as err:
                print(err)
                continue

    if int(choice) == 3:
        inner_choice = input('1 - List of all authors\n'
                             '2 - Get author info\n'
                             'Your choice: ')

        try:
            validate_choice(choice=inner_choice, start=1, stop=2)
        except InvalidChoice as err:
            print(err)
            continue

        if int(inner_choice) == 1:
            res = AuthorsService(
                db_provider(DB_NAME, DB_TYPE)
            ).get_all_authors_info()
            print(res)

        if int(inner_choice) == 2:
            author_id = input('Enter book id: ')

            try:
                validate_id(author_id)
                res = AuthorsService(
                    db_connector=db_provider(DB_NAME, DB_TYPE)
                ).get_author_info(int(author_id))
                print(res)
            except NotDigitError as err:
                print(err)
                continue
            except InvalidIdError as err:
                print(err)
                continue

    if int(choice) == 4:
        res = TransactionsService(db_provider(DB_NAME, DB_TYPE)).get_info()
        print(res)

    if int(choice) == 5:
        print('Goodbye!')
        break
