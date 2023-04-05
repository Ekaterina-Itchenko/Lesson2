from random import uniform, randint
from faker import Faker
from time import time
from typing import TYPE_CHECKING, TypeVar, ParamSpec, Callable, Any
from DTO import CompanyDTO
if TYPE_CHECKING:
    from interfaces import DbProto
    from data_access import CompaniesInfo


RT = TypeVar('RT')
P = ParamSpec('P')

cache: dict[Any, tuple[float, Any]] = {}


def use_cache(live_time: int = 10) -> Callable[[Callable[P, RT]],
                                               Callable[P, RT]]:
    def wrap(func: Callable[P, RT]) -> Callable[P, RT]:
        """Decorator for using cache"""

        def wrapper(*args: P.args, **kwargs: P.kwargs) -> RT | Any:
            now = time()
            if args not in cache or now - cache[args][0] > live_time:
                value = func(*args, **kwargs)
                cache[args] = (now, value)
            return cache[args][1]
        return wrapper
    return wrap


@use_cache()
def find_info(text: str, db_connector: 'DbProto') -> 'CompaniesInfo':
    companies = []
    for company in db_connector.get_file_information():
        if text.lower() in company.name.lower():
            companies.append(company)
    return companies


@use_cache()
def get_companies_by_sector(sector: str,
                            db_connector: 'DbProto') -> 'CompaniesInfo':
    return list(filter(lambda comp: sector.lower() == comp.sector.lower(),
                       db_connector.get_file_information()))


def calculate_average_price(db_connector: 'DbProto') -> float:
    total_price = 0.0
    for company in db_connector.get_file_information():
        total_price += company.price
    return round(total_price /
                 len(db_connector.get_file_information()), 4)


def get_top_10_companies(db_connector: 'DbProto') -> list:
    sorted_lst = sorted(db_connector.get_file_information(),
                        key=lambda dct: dct.price, reverse=True)
    return [(company.name, company.price) for company in sorted_lst[:10]]


@use_cache()
def add_new_company(symbol: str, new_name: str, sector: str,
                    price: float, db_connector: 'DbProto') -> None:
    new_line = CompanyDTO(symbol=symbol,
                          name=new_name,
                          sector=sector,
                          price=price)
    db_connector.record_new_line(new_line)


@use_cache()
def update_company_name(symbol: str, new_name: str,
                        db_connector: 'DbProto') -> None:
    companies = db_connector.get_file_information()
    for company in companies:
        if company.symbol.lower() == symbol.lower():
            company.name = new_name
    db_connector.record_new_information(companies)


@use_cache()
def delete_company(symbol: str, db_connector: 'DbProto') -> None:
    companies = db_connector.get_file_information()
    for company in companies:
        if company.symbol.lower() == symbol.lower():
            index = companies.index(company)
            del companies[index]
    db_connector.record_new_information(companies)


def truncate_all(db_connector: 'DbProto') -> None:
    file: list = []
    db_connector.record_new_information(file)


def take_random_symbol() -> str:
    letters_list = []
    fake = Faker()
    for _ in range(randint(3, 6)):
        letters_list.append(fake.random_uppercase_letter())
    return ''.join(letters_list)


@use_cache()
def generate_random_data(number: str, db_connector: 'DbProto') -> None:
    new_information = []
    fake = Faker()
    for _ in range(int(number)):
        new_information.append(CompanyDTO(symbol=take_random_symbol(),
                                          name=fake.company(),
                                          sector=fake.catch_phrase(),
                                          price=uniform(0, 1000)))
    db_connector.record_new_information(new_information)
