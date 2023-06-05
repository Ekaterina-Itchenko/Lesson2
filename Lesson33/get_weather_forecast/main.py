from prettytable import PrettyTable
from validations import validate_user_choice
from errors import ChoiceError
from config import API_NAME
from providers import provide_api


if __name__ == '__main__':
    while True:
        choice = input("1 - Get weather\n2 - Exit\nYour choice: ")
        try:
            validate_user_choice(user_choice=choice)
        except ChoiceError as err:
            print(err)
            continue

        if choice == '2':
            break
        if choice == '1':
            cities = input('Enter cities separated by coma: ').split(',')
            table = PrettyTable()
            table.field_names = ["city", "temp", "description", "humidity"]
            for city in cities:
                try:
                    weather = provide_api(api_name=API_NAME,
                                          city=city.strip()).get_weather()
                    table.add_row([weather.city,
                                   weather.temperature,
                                   weather.desc,
                                   weather.humidity])
                except KeyError:
                    print(f"Wrong city name: {city}")
                except ValueError as err:
                    print(err)
            print(table)
