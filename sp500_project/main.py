from business_logic import (find_info,
                            get_companies_by_sector,
                            calculate_average_price,
                            get_top_10_companies,
                            add_new_company,
                            update_company_name,
                            delete_company,
                            generate_random_data,
                            truncate_all)
from validators import (validator,
                        check_name,
                        check_price,
                        check_symbol,
                        check_generation_number,
                        check_name_uniqueness,
                        check_symbol_existence,
                        check_sector_existence,
                        check_symbol_uniqueness)
from errors import (NotDigitError,
                    UnexpectedNumberError,
                    WrongSymbolError,
                    WrongNameLengthError,
                    WrongPriceError,
                    WrongGenerationNumberError,
                    NoSuchSymbolError,
                    WrongSectorError,
                    CompanyAlreadyExistsError)
from providers import provider
from config import DB_TYPE, DATA_BASE


while True:
    choice = input('Choose the action from menu:\n'
                   '1 - Find info by name\n'
                   '2 - Get all companies by sector\n'
                   '3 - Calculate average price\n'
                   '4 - Get top 10 companies\n'
                   '5 - Exit\n'
                   '6 - Add new company\n'
                   '7 - Update company name\n'
                   '8 - Delete company\n'
                   '9 - Truncate all\n'
                   '10 - Populate file with random data_access\n'
                   'Your choice: '
                   )

    try:
        validator(choice)
    except NotDigitError as err:
        print(err)
        continue
    except UnexpectedNumberError as err:
        print(err)
        continue

    if int(choice) == 1:
        name = input('Enter the name of company: ')
        print(find_info(name, provider(DB_TYPE, DATA_BASE)))

    elif int(choice) == 2:
        sector = input('Enter the name of Sector: ')
        print(get_companies_by_sector(sector, provider(DB_TYPE, DATA_BASE)))

    elif int(choice) == 3:
        print(calculate_average_price(provider(DB_TYPE, DATA_BASE)))

    elif int(choice) == 4:
        print(get_top_10_companies(provider(DB_TYPE, DATA_BASE)))

    elif int(choice) == 5:
        print('GOODBYE')
        break

    elif int(choice) == 6:
        symbol = input('Enter the symbol of company: ')
        try:
            check_symbol(symbol=symbol)
            check_symbol_uniqueness(symbol, provider(DB_TYPE, DATA_BASE))
        except WrongSymbolError as err:
            print(err)
            continue
        except CompanyAlreadyExistsError as err:
            print(err)
            continue

        sector = input('Enter the Sector: ')
        try:
            check_sector_existence(sector, provider(DB_TYPE, DATA_BASE))
        except WrongSectorError as err:
            print(err)
            continue

        name = input('Enter the name of company: ')
        try:
            check_name(name=name)
            check_name_uniqueness(name, provider(DB_TYPE, DATA_BASE))
        except WrongNameLengthError as err:
            print(err)
            continue
        except CompanyAlreadyExistsError as err:
            print(err)
            continue

        price = input('Enter the price: ')
        try:
            check_price(price=price)
        except WrongPriceError as err:
            print(err)
            continue
        add_new_company(symbol=symbol, new_name=name,
                        price=float(price), sector=sector,
                        db_connector=provider(DB_TYPE, DATA_BASE))
        print('The new company has added')

    elif int(choice) == 7:
        symbol = input('Enter the symbol of company: ')
        try:
            check_symbol_existence(symbol, provider(DB_TYPE, DATA_BASE))
        except NoSuchSymbolError as err:
            print(err)
            continue

        name = input('Enter a new name of company: ')
        try:
            check_name(name=name)
            check_name_uniqueness(name, provider(DB_TYPE, DATA_BASE))
        except WrongNameLengthError as err:
            print(err)
            continue
        except CompanyAlreadyExistsError as err:
            print(err)
            continue

        update_company_name(symbol, name, provider(DB_TYPE, DATA_BASE))
        print('The company name has updated.')

    elif int(choice) == 8:
        symbol = input('Enter the symbol of company: ')
        try:
            check_symbol_existence(symbol, provider(DB_TYPE, DATA_BASE))
        except NoSuchSymbolError as err:
            print(err)
            continue
        delete_company(symbol, provider(DB_TYPE, DATA_BASE))
        print('The company has deleted.')

    elif int(choice) == 9:
        truncate_all(provider(DB_TYPE, DATA_BASE))
        print('The all information has deleted.')

    elif int(choice) == 10:
        number = input('Enter a number of records for generation: ')
        try:
            check_generation_number(number)
        except WrongGenerationNumberError as err:
            print(err)
            continue

        generate_random_data(number, provider(DB_TYPE, DATA_BASE))
        print('A new random data has generated.')
