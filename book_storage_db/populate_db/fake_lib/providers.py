from __future__ import annotations
from random import randint, choice, uniform
import string
import json
from datetime import date, datetime, timedelta
from typing import Any, Optional


class EmailProvider:
    def __call__(self) -> str:
        letters = string.ascii_letters
        domens = ['gmail.com', 'mail.ru', 'yandex.ru', 'yahoo.com']
        name = ''
        for number in range(randint(8, 15)):
            letter = letters[randint(0, len(letters) - 1)]
            name += letter
        return f'{name}@{choice(domens)}'


class PhoneProvider:
    def _get_digit(self) -> str:
        digits = string.digits
        return choice(digits)

    def __call__(self) -> str:
        code = ['29', '33', '44']
        return f"+375 {choice(code)}" \
               f" {''.join([self._get_digit() for _ in range(7)])}"


class BankCardProvider:
    def _get_digit(self) -> str:
        digits = string.digits
        return choice(digits)

    def __call__(self) -> int:
        return int(f"{''.join([self._get_digit() for _ in range(16)])}")


class NameProvider:
    def __call__(self) -> str:
        with open('data/first_names.json', encoding='utf8') as file:
            popular_names = json.load(file)
        return choice(popular_names)


class LastNameProvider:
    def __call__(self) -> str:
        with open('data/last_names.json', encoding='utf8') as file:
            surname_list = json.load(file)
        return choice(surname_list)


class DateProvider:
    def __call__(self, first_date: datetime = None) -> Optional[object]:
        year = randint(1800, 2010)
        month = randint(1, 12)
        if (month <= 7 and month % 2 != 0) or (month >= 8 and month % 2 == 0):
            day = randint(1, 31)
        elif ((month <= 6 and month % 2 == 0 and month != 2)
              or (month >= 9 and month % 2 != 0)):
            day = randint(1, 30)
        else:
            day = randint(1, 28)
        if day < 10:
            day = f'0{day}'
        if month < 10:
            month = f'0{month}'
        random_date = datetime.strptime(f'{year}-{month}-{day}',
                                        '%Y-%m-%d').date()
        if first_date is not None:
            max_days = (datetime.today().date() - first_date).days
            max_year = max_days / 365
            if 100 > max_year > 25:
                number = randint(25 * 365, max_days)
                res = first_date + timedelta(days=number)
                return res
            elif 100 < max_year:
                number = randint(25 * 365, 100 * 365)
                res = first_date + timedelta(days=number)
                return res
            else:
                return None
        return random_date


class TextProvider:
    def __call__(self) -> str:
        with open('data/words_list.json', encoding='utf8') as file:
            words_list = json.load(file)
        return ' '.join([choice(words_list) for _ in
                         range(choice(range(5, 20)))])


class TitleBookProvider:
    def __call__(self) -> str:
        with open('data/words_list.json', encoding='utf8') as file:
            words_list = json.load(file)
        return ' '.join([choice(words_list) for _ in
                         range(choice(range(1, 4)))])


class GenreProvider:
    def __call__(self) -> str:
        genres_list = [
            "Fantasy",
            "Adventure",
            "Romance",
            "Contemporary",
            "Dystopian",
            "Mystery",
            "Horror",
            "Thriller",
            "Paranormal",
            "Historical-fiction",
            "Science-fiction",
            "Children’s",
            "Memoir",
            "Cookbook",
            "Art",
            "Development",
            "Motivational",
            "Health",
            "History",
            "Travel",
            "Families & Relationships",
            "Humor",
            "Mystery",
            "Westerns"
        ]
        return choice(genres_list)


class RoleProvider:
    def __call__(self) -> str:
        roles = ["administrator", "moderator", "manager", "user"]
        return choice(roles)


class PermissionProvider:
    def __call__(self) -> str:
        permissions = ["Read Only", "Create", "Update", "Full access"]
        return choice(permissions)


class DigitProvider:
    def __call__(self) -> int:
        return randint(0, 99)


class PasswordProvider:
    def __call__(self) -> str:
        number = randint(8, 15)
        return ''.join([choice(string.ascii_letters) for _ in range(number)])


class FloatDigitProvider:
    def __call__(self) -> float:
        return round(uniform(1, 1000), 2)


class BookFormatProvider:
    def __call__(self) -> str:
        formats = ["hardcover", "paper cover", 'e-book']
        return choice(formats)


class CountryProvider:
    def __call__(self) -> str:
        countries = ['Belarus', 'Poland']
        return choice(countries)


class CityProvider:
    def __call__(self, country: str) -> str:
        if country == "Belarus":
            with open('data/belarus_cities.json', encoding='utf8') as file:
                belarus_cities = json.load(file)
            return choice(belarus_cities)
        if country == "Poland":
            with open('data/poland_cities.json', encoding='utf8') as file:
                poland_cities = json.load(file)
            return choice(poland_cities)


class WordProvider:
    def __call__(self) -> str:
        with open('data/words_list.json', encoding='utf8') as file:
            words = json.load(file)
            return choice(words)


class RandomIdProvider:
    def __init__(self, id_list: list[Any]) -> None:
        self._id_list = id_list

    def __call__(self) -> int:
        random_value = choice(self._id_list)
        if isinstance(random_value, tuple):
            return random_value[0]
        return random_value


class BasketStatusProvider:
    def __call__(self) -> str:
        statuses = ['Paid', 'Archived', 'Pending', 'Active']
        return choice(statuses)


class CvcProvider:
    def __call__(self) -> int:
        return randint(100, 999)


class ExpiryDateProvider:
    def __call__(self) -> str:
        current_year = date.today().year
        year = randint(current_year, current_year + 3)
        month = randint(1, 12)
        if month < 10:
            month = f'0{month}'
        return f'{month} {year}'
