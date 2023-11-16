from errors import (NotDigitError,
                    UnexpectedNumberError,
                    CategoryExistenceError,
                    InvalidCategoryError,
                    InvalidIdError,
                    DigitError)
from validation import validator_choice, check_id, check_amount
from business_logic import (add_category,
                            get_parameters,
                            add_new_goods,
                            get_info_of_goods,
                            get_specific_product,
                            make_order,
                            get_statistic)
from config import ST_FILE, CT_FILE, ORD_FILE, DB_TYPE
from providers import provide_st, provide_ord, provide_ct
from typing import Optional


parameters: Optional[list[str]] | str

while True:
    choice = input('Choose the action:\n'
                   '1 - Create a category of goods\n'
                   '2 - Add a new goods\n'
                   '3 - Get a list of all items in the storage\n'
                   '4 - Get a specific item\n'
                   '5 - Make an order\n'
                   '6 - Get statistics\n'
                   '7 - Exit\n'
                   'Your choice: ')

    try:
        validator_choice(choice)
    except NotDigitError as err:
        print(err)
        continue
    except UnexpectedNumberError as err:
        print(err)
        continue

    if int(choice) == 1:
        category = input('Enter a category: ')
        parameters = input('Enter valid parameters: ')
        try:
            add_category(category, parameters,
                         provide_ct(DB_TYPE, CT_FILE))
            print('The category has added.')
        except CategoryExistenceError as err:
            print(err)
            continue

    elif int(choice) == 2:
        category = input('Enter a category: ')
        try:
            parameters = get_parameters(category, provide_ct(DB_TYPE,
                                                             CT_FILE))
            if not parameters:
                raise ValueError("The category is not exist.")
            result_info: dict[str, str] = {}
            for parameter in parameters:
                value = input(f'Enter {parameter}: ')
                result_info[parameter] = value
            amount_of_goods = input('Enter amount of goods '
                                    'that arrived at the storage: ')
            check_amount(amount_of_goods)
            add_new_goods(result_info, amount_of_goods,
                          category, provide_st(DB_TYPE, ST_FILE))
        except InvalidCategoryError as err:
            print(err)
            continue
        except NotDigitError as err:
            print(err)
            continue
        except DigitError as err:
            print(err)
            continue
        except ValueError as err:
            print(err)
            continue

    elif int(choice) == 3:
        try:
            category = input('Enter a category: ')

            min_created_date = input('Enter minimum date of addition'
                                     ' in following format - "YYYY-MM-DD": ')
            max_created_data = input('Enter maximum date of addition'
                                     ' in following format - "YYYY-MM-DD": ')
            get_info_of_goods(category, min_created_date,
                              max_created_data, provide_st(DB_TYPE, ST_FILE),
                              provide_ct(DB_TYPE, CT_FILE))
        except InvalidCategoryError as err:
            print(err)
            continue
        except ValueError:
            print('Invalid date format.')
            continue

    elif int(choice) == 4:
        try:
            product_id = input('Enter an "id" of product: ')
            check_id(product_id)
            get_specific_product(product_id, provide_st(DB_TYPE, ST_FILE))
        except NotDigitError as err:
            print(err)
            continue
        except InvalidIdError as err:
            print(err)
            continue

    elif int(choice) == 5:
        id_list = input('Enter a list of product id and their quantities'
                        ' separated by commas in following format'
                        ' <"id" "quantity", "id" "quantity", ...> : ')
        try:
            print(make_order(id_list, provide_st(DB_TYPE, ST_FILE),
                             provide_ord(DB_TYPE, ORD_FILE)))
        except InvalidIdError as err:
            print(err)
            continue
        except ValueError:
            print('Id and quantity of good must be digits.'
                  ' Order input format must be'
                  ' <"id" "quantity", "id" "quantity", ...>')

    elif int(choice) == 6:
        min_date = input('Enter minimum date'
                         ' in following format - "YYYY-MM-DD": ')
        max_date = input('Enter maximum date '
                         'in following format - "YYYY-MM-DD": ')
        try:
            get_statistic(min_date, max_date, provide_st(DB_TYPE, ST_FILE),
                          provide_ord(DB_TYPE, ORD_FILE),
                          provide_ct(DB_TYPE, CT_FILE))
        except ValueError:
            print('Invalid date format.')
            continue

    elif int(choice) == 7:
        print('GOODBYE')
        break
