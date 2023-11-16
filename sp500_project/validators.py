from errors import (NotDigitError,
                    UnexpectedNumberError,
                    WrongSymbolError,
                    WrongNameLengthError,
                    WrongPriceError,
                    WrongGenerationNumberError,
                    NoSuchSymbolError,
                    WrongSectorError,
                    CompanyAlreadyExistsError)
from string import ascii_uppercase
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from interfaces import DbProto


def validator(choice: str) -> None:
    if not choice.isdigit():
        raise NotDigitError('Your choice must be a digit.')
    elif int(choice) not in range(1, 11):
        raise UnexpectedNumberError('Enter a digit from 1 to 5')


def check_symbol(symbol: str) -> None:
    if symbol.upper() != symbol:
        raise WrongSymbolError('The letters should be in the upper register.')
    if len(symbol) < 3 or len(symbol) > 6:
        raise WrongSymbolError('The letters length should be from 3 to 6.')
    for letter in symbol:
        if letter not in ascii_uppercase:
            raise WrongSymbolError('The letters should be in ascii')


def check_name(name: str) -> None:
    if len(name) < 3 or len(name) > 50:
        raise WrongNameLengthError('The length of company'
                                   ' name should be from 3 to 50.')


def check_price(price: str) -> None:
    if float(price) < 0 or float(price) > 1000:
        raise WrongPriceError('The price should be from 0 to 1000.')
    if '.' not in price:
        raise WrongPriceError('The price should be float')


def check_generation_number(number: str) -> None:
    if not number.isdigit():
        raise WrongGenerationNumberError('A generation number '
                                         'must be a digit.')
    if int(number) < 0 or int(number) > 10000:
        raise WrongGenerationNumberError('A generation number '
                                         'should be from 0 to 10000.')


def check_symbol_uniqueness(symbol: str, db_connector: 'DbProto') -> None:
    file = db_connector.get_file_information()
    if symbol.lower() in map(lambda dct: dct.symbol.lower(), file):
        raise CompanyAlreadyExistsError('This symbol of'
                                        ' company already exists.')


def check_symbol_existence(symbol: str, db_connector: 'DbProto') -> None:
    file = db_connector.get_file_information()
    if symbol.lower() not in map(lambda dct:
                                 dct.symbol.lower(), file):
        raise NoSuchSymbolError('Company with this symbol is not exist.')


def check_name_uniqueness(name: str, db_connector: 'DbProto') -> None:
    file = db_connector.get_file_information()
    if name.lower() in map(lambda dct: dct.name.lower(), file):
        raise CompanyAlreadyExistsError('This company name already exists.')


def check_sector_existence(sector: str, db_connector: 'DbProto') -> None:
    file = db_connector.get_file_information()
    if sector.lower() not in map(lambda dct: dct.sector.lower(), file):
        raise WrongSectorError('This sector is not exist.')
