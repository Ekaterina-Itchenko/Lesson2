import json
import sqlite3


def full_sqlite_db_from_json_file(file_name: str, db_name: str) -> None:
    with open(file_name, encoding='utf8') as file:
        companies_list = tuple(json.load(file))
    connector = sqlite3.connect(db_name)
    cursor = connector.cursor()
    cursor.executemany(
        'INSERT INTO companies (symbol, name, sector, price) '
        'VALUES (:Symbol, :Name, :Sector, :Price)', companies_list
    )
    connector.commit()


full_sqlite_db_from_json_file('sp500.json', 'sp500.db')
