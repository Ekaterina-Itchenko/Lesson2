from errors import (NotDigitError,
                    UnexpectedNumberError,
                    WrongSymbolError,
                    CompanyAlreadyExistsError,
                    WrongNameLengthError,
                    WrongSectorError,
                    WrongPriceError,
                    NoSuchSymbolError,
                    WrongGenerationNumberError)
from string import ascii_uppercase


def validator(choice: str):
    if not choice.isdigit():
        raise NotDigitError('Your choice must be a digit.')
    elif int(choice) not in range(1, 11):
        raise UnexpectedNumberError('Enter a digit from 1 to 5')


def check_symbol(symbol: str):
    if symbol.upper() != symbol:
        raise WrongSymbolError('The letters should be in the upper register.')
    if len(symbol) < 3 or len(symbol) > 6:
        raise WrongSymbolError('The letters length should be from 3 to 6.')
    for letter in symbol:
        if letter not in ascii_uppercase:
            raise WrongSymbolError('The letters should be in ascii')


def check_symbol_uniqueness(symbol: str, file: list):
    if symbol.lower() in map(lambda dct: dct.get('Symbol').lower(), file):
        raise CompanyAlreadyExistsError('This company already exists.')


def check_symbol_existence(symbol, file):
    if symbol.lower() not in map(lambda dct: dct.get('Symbol').lower(), file):
        raise NoSuchSymbolError('Company with this symbol is not exist.')


def check_name(name: str):
    if len(name) < 3 or len(name) > 50:
        raise WrongNameLengthError('The length of company'
                                   ' name should be from 3 to 50.')


def check_name_uniqueness(name: str, file: list):
    if name.lower() in map(lambda dct: dct.get('Name').lower(), file):
        raise CompanyAlreadyExistsError('This company already exists.')


def check_sector(sector: str, file: list):
    if sector.lower() not in map(lambda dct: dct.get('Sector').lower(), file):
        raise WrongSectorError('This sector is not exist.')


def check_price(price: str):
    if float(price) < 0 or float(price) > 1000:
        raise WrongPriceError('The price should be from 0 to 1000.')
    if '.' not in price:
        raise WrongPriceError('The price should be float')


def check_generation_number(number: str):
    if not number.isdigit():
        raise WrongGenerationNumberError('A generation number '
                                         'must be a digit.')
    if int(number) < 0 or int(number) > 10000:
        raise WrongGenerationNumberError('A generation number '
                                         'should be from 0 to 10000.')
