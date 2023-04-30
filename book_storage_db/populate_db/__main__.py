import sys
import os
from data_access import SqliteConnector
from data_access.dao import (
    AuthorsDAO,
    GenresDAO,
    RolesDAO,
    PermissionsDAO,
    TransactionsDAO,
    AddressesDAO,
    BankcardsDAO,
    BooksDAO,
    BasketsDAO,
    UsersDAO,
    UsersAddressesDAO,
    UsersBankcardsDAO,
    UsersRolesDAO,
    BasketsBooksDAO,
    BooksAuthorsDAO,
    BooksGenresDAO,
    PermissionsRolesDAO
)
from factories import (
    AuthorsFactory,
    GenresFactory,
    BankcardsFactory,
    BasketsFactory,
    BooksFactory,
    AddressesFactory,
    PermissionsFactory,
    TransactionsFactory,
    RolesFactory,
    UsersFactory,
    BooksGenresFactory,
    BooksAuthorsFactory,
    BasketsBooksFactory,
    UsersBankcardsFactory,
    UsersRolesFactory,
    UsersAddressesFactory,
    PermissionsRolesFactory

)
from fake_lib import (
    PhoneProvider,
    NameProvider,
    EmailProvider,
    BankCardProvider,
    LastNameProvider,
    TextProvider,
    DateProvider,
    GenreProvider,
    RoleProvider,
    PermissionProvider,
    DigitProvider,
    PasswordProvider,
    FloatDigitProvider,
    BookFormatProvider,
    TitleBookProvider,
    CountryProvider,
    CityProvider,
    WordProvider,
    RandomIdProvider,
    BasketStatusProvider,
    CvcProvider,
    ExpiryDateProvider,
    AvailableIdProvider

)
from populate_command import PopulateTable

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

if __name__ == '__main__':

    arguments = sys.argv[1:]
    for index in range(0, len(arguments), 2):
        if arguments[index] not in ('-n', '-d'):
            raise ValueError('Invalid index.')
        if arguments[index] == '-d':
            db_name = arguments[index + 1]
        if arguments[index] == '-n':
            records_number = int(arguments[index + 1])

    db_connector = SqliteConnector(db_name=db_name)

    authors_dao = AuthorsDAO(db_connector=db_connector)
    author_factory = AuthorsFactory(first_name=NameProvider(),
                                    last_name=LastNameProvider(),
                                    birth_date=DateProvider(),
                                    death_date=DateProvider(),
                                    information=TextProvider())
    PopulateTable(records_number=records_number,
                  dao=authors_dao,
                  fake_factory=author_factory).execute()
    author_id_list = authors_dao.get_id_list()

    genres_dao = GenresDAO(db_connector=db_connector)
    genres_factory = GenresFactory(genre_name=GenreProvider(),
                                   genre_description=TextProvider())
    PopulateTable(records_number=records_number,
                  dao=genres_dao,
                  fake_factory=genres_factory).execute()
    genre_id_list = genres_dao.get_id_list()

    roles_dao = RolesDAO(db_connector=db_connector)
    roles_factory = RolesFactory(role_name=RoleProvider())
    PopulateTable(records_number=records_number,
                  dao=roles_dao,
                  fake_factory=roles_factory).execute()
    role_id_list = roles_dao.get_id_list()

    permissions_dao = PermissionsDAO(db_connector=db_connector)
    permissions_factory = PermissionsFactory(
        permission_name=PermissionProvider()
    )
    PopulateTable(records_number=records_number,
                  dao=permissions_dao,
                  fake_factory=permissions_factory).execute()
    permission_id_list = permissions_dao.get_id_list()

    permissions_roles_dao = PermissionsRolesDAO(db_connector=db_connector)
    permissions_roles_factory = PermissionsRolesFactory(
        permission_id=RandomIdProvider(permission_id_list),
        role_id=RandomIdProvider(role_id_list)
    )
    PopulateTable(records_number=records_number,
                  dao=permissions_roles_dao,
                  fake_factory=permissions_roles_factory).execute()

    books_dao = BooksDAO(db_connector=db_connector)
    books_factory = BooksFactory(title=TitleBookProvider(),
                                 price=FloatDigitProvider(),
                                 description=TextProvider(),
                                 pages=DigitProvider(),
                                 book_format=BookFormatProvider(),
                                 age_limit=DigitProvider(),
                                 amount=DigitProvider())
    PopulateTable(records_number=records_number,
                  dao=books_dao,
                  fake_factory=books_factory).execute()
    books_id_list = books_dao.get_id_list()

    books_authors_dao = BooksAuthorsDAO(db_connector=db_connector)
    books_authors_factory = BooksAuthorsFactory(
        book_id=RandomIdProvider(books_id_list),
        author_id=RandomIdProvider(author_id_list)
    )
    PopulateTable(records_number=records_number,
                  dao=books_authors_dao,
                  fake_factory=books_authors_factory).execute()

    books_genres_dao = BooksGenresDAO(db_connector=db_connector)
    books_genres_factory = BooksGenresFactory(
        book_id=RandomIdProvider(books_id_list),
        genre_id=RandomIdProvider(genre_id_list)
    )
    PopulateTable(records_number=records_number,
                  dao=books_genres_dao,
                  fake_factory=books_genres_factory).execute()

    users_dao = UsersDAO(db_connector=db_connector)
    users_factory = UsersFactory(first_name=NameProvider(),
                                 last_name=LastNameProvider(),
                                 user_name=NameProvider(),
                                 age=DigitProvider(),
                                 email=EmailProvider(),
                                 phone_number=PhoneProvider(),
                                 password=PasswordProvider())
    PopulateTable(records_number=records_number,
                  dao=users_dao,
                  fake_factory=users_factory).execute()
    users_id_list = users_dao.get_id_list()

    addresses_dao = AddressesDAO(db_connector=db_connector)
    addresses_factory = AddressesFactory(country=CountryProvider(),
                                         city=CityProvider(),
                                         street=WordProvider(),
                                         home_number=DigitProvider(),
                                         post_code=DigitProvider())
    PopulateTable(records_number=records_number,
                  dao=addresses_dao,
                  fake_factory=addresses_factory).execute()
    address_id_list = addresses_dao.get_id_list()

    users_roles_dao = UsersRolesDAO(db_connector=db_connector)
    users_roles_factory = UsersRolesFactory(
        user_id=RandomIdProvider(users_id_list),
        role_id=RandomIdProvider(role_id_list)
    )
    PopulateTable(records_number=records_number,
                  dao=users_roles_dao,
                  fake_factory=users_roles_factory).execute()

    users_addresses_dao = UsersAddressesDAO(db_connector=db_connector)
    users_addresses_factory = UsersAddressesFactory(
        user_id=RandomIdProvider(users_id_list),
        address_id=RandomIdProvider(address_id_list)
    )
    PopulateTable(records_number=records_number,
                  dao=users_addresses_dao,
                  fake_factory=users_addresses_factory).execute()

    bankcards_dao = BankcardsDAO(db_connector=db_connector)
    bankcards_factory = BankcardsFactory(
        number=BankCardProvider(),
        first_name=NameProvider(),
        last_name=LastNameProvider(),
        cvc=CvcProvider(),
        expiry_date=ExpiryDateProvider()
    )
    PopulateTable(records_number=records_number,
                  dao=bankcards_dao,
                  fake_factory=bankcards_factory).execute()
    bankcard_id_list = bankcards_dao.get_id_list()

    users_bankcards_dao = UsersBankcardsDAO(db_connector=db_connector)
    users_bankcards_factory = UsersBankcardsFactory(
        user_id=RandomIdProvider(users_id_list),
        bankcard_id=RandomIdProvider(bankcard_id_list)
    )
    PopulateTable(records_number=records_number,
                  dao=users_bankcards_dao,
                  fake_factory=users_bankcards_factory).execute()

    baskets_dao = BasketsDAO(db_connector=db_connector)
    baskets_factory = BasketsFactory(
        user_id=RandomIdProvider(users_id_list),
        status=BasketStatusProvider()
    )
    PopulateTable(records_number=records_number,
                  dao=baskets_dao,
                  fake_factory=baskets_factory).execute()
    basket_id_list = baskets_dao.get_id_list()

    baskets_books_dao = BasketsBooksDAO(db_connector=db_connector)
    baskets_books_factory = BasketsBooksFactory(
        basket_id=RandomIdProvider(basket_id_list),
        book_id=RandomIdProvider(books_id_list),
        quantity=DigitProvider()
    )
    PopulateTable(records_number=records_number,
                  dao=baskets_books_dao,
                  fake_factory=baskets_books_factory).execute()

    transactions_dao = TransactionsDAO(db_connector=db_connector)
    bc_available_id_list = bankcards_dao.get_available_id_list_for_transact()
    available_address_list = addresses_dao.get_available_id_list_for_transact()
    transactions_factory = TransactionsFactory(
        basket_id=RandomIdProvider(basket_id_list),
        bankcard_id=AvailableIdProvider(bc_available_id_list),
        amount=FloatDigitProvider(),
        address_id=AvailableIdProvider(available_address_list)
    )
    PopulateTable(records_number=records_number,
                  dao=transactions_dao,
                  fake_factory=transactions_factory).execute()
