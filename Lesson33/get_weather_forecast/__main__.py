from prettytable import PrettyTable
from validations import validate_user_choice
from errors import ChoiceError
from config import API_URL
from providers import provide_api
from requests import Session
from service import WeatherService
from DTO import WeatherConditionsDTO


def create_table(table: PrettyTable,
                 data: WeatherConditionsDTO) -> None:
    if not table.field_names:
        table.field_names = ["city", "temp", "description", "humidity"]
    city_weather_data = [
        data.name,
        data.main.temp,
        data.weather[0].description,
        data.main.humidity
    ]
    table.add_row(row=city_weather_data)


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
            cities = input('Enter cities separated by coma: ')
            table = PrettyTable()
            with Session() as session:
                try:
                    cities_weather = WeatherService(
                        api_adapter=provide_api(
                            api_url=API_URL,
                            session=session
                        )
                    ).get_weather_in_cities(cities=cities)
                    for city_weather in cities_weather:
                        create_table(table=table,
                                     data=city_weather)
                    print(table)
                except ValueError as err:
                    print(err)
                    continue
