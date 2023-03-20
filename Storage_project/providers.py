from data_access import StorageJson, CategoriesJson, OrdersJson


def provide_st(db_type, db_file):
    if db_type == "json":
        return StorageJson(db_file)
    else:
        raise ValueError("Unsupported DB type.")


def provide_ct(db_type, db_file):
    if db_type == "json":
        return CategoriesJson(db_file)
    else:
        raise ValueError("Unsupported DB type.")


def provide_ord(db_type, db_file):
    if db_type == "json":
        return OrdersJson(db_file)
    else:
        raise ValueError("Unsupported DB type.")
