from data_access.data import Sp500Csv, Sp500Json


def provider(file_extension, db_name):
    if file_extension == '.csv':
        return Sp500Csv(db_name)
    elif file_extension == '.json':
        return Sp500Json(db_name)
