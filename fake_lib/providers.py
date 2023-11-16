from random import randint, choice
import string


class EmailProvider:
    def __call__(self, *args, **kwargs):
        letters = string.ascii_letters
        domens = ['gmail.com', 'mail.ru', 'yandex.ru', 'yahoo.com']
        name = ''
        for number in range(randint(8, 15)):
            letter = letters[randint(0, len(letters) - 1)]
            name += letter
        return f'{name}@{choice(domens)}'


class PhoneProvider:
    @staticmethod
    def get_digit():
        digits = string.digits
        return choice(digits)

    def __call__(self, *args, **kwargs):
        code = ['29', '33', '44']
        return f"+375 {choice(code)}" \
               f" {''.join([self.get_digit() for _ in range(7)])}"


class BankCardProvider:
    @staticmethod
    def get_digit():
        digits = string.digits
        return choice(digits)

    def __call__(self, *args, **kwargs):
        return f"{''.join([self.get_digit() for _ in range(16)])}"


class NameProvider:
    def __call__(self, *args, **kwargs):
        popular_names = ['Mary', 'Kate', 'Igor', 'Alexander',
                         'Alexey', 'Olga', 'Maxim', 'Peter', 'Nikolay']
        return choice(popular_names)
