from data_access import record_to_exel_sheets
from errors import (CategoryExistenceError,
                    InvalidCategoryError,
                    InvalidIdError)
from datetime import date


def add_category(category: str, parameters: str, ct_connector):
    for item in ct_connector.get_all_categories().keys():
        if item.lower() == category.lower():
            raise CategoryExistenceError("This category has already exists.")
    parameters_list = [element.strip().lower() for
                       element in parameters.split(',')]
    if 'price' not in parameters_list:
        parameters_list.append('price')
    if 'name' not in parameters_list:
        parameters_list.append('name')
    ct_connector.record_new_category(category, parameters_list)


def get_parameters(category: str, ct_connector) -> list:
    if category.lower() not in [item.lower()
                                for item in
                                ct_connector.get_all_categories().keys()]:
        raise InvalidCategoryError("This category is not exist.")
    return ct_connector.get_all_categories()[category]


def add_new_goods(info: dict, amount_of_goods: str,
                  category: str, st_connector):
    info['category'] = category
    storage = st_connector.get_storage_info()
    goods_list = storage['Goods']
    flag = True
    for product in goods_list:
        if set(info.items()).issubset(set(product.items())):
            product["quantity"] += int(amount_of_goods)
            product["updated_at"] = str(date.today())
            storage["Goods"] = goods_list
            st_connector.record_with_new_info(storage)
            flag = False
    if flag:
        info['quantity'] = int(amount_of_goods)
        info["created_at"] = str(date.today())
        info["updated_at"] = str(date.today())
        info["id"] = len(goods_list) + 1
        goods_list.append(info)
        storage["Goods"] = goods_list
        st_connector.record_with_new_info(storage)


def get_info_of_goods(category, min_date, max_date,
                      st_connector, ct_connector):
    all_goods = st_connector.get_storage_info()['Goods']
    if category.strip():
        if (category.lower() not in
                [item.lower() for item in
                 ct_connector.get_all_categories().keys()]):
            raise InvalidCategoryError("This category is not exist.")
        result = []
        for product in all_goods:
            if product['category'].lower() == category.lower():
                result.append(product)
        all_goods = result
    if min_date.strip():
        result = []
        for product in all_goods:
            if (date.fromisoformat(product['created_at']) >=
                    date.fromisoformat(min_date.strip())):
                result.append(product)
        all_goods = result
    if max_date.strip():
        result = []
        for product in all_goods:
            if (date.fromisoformat(product['created_at']) <=
                    date.fromisoformat(max_date.strip())):
                result.append(product)
        all_goods = result
    if all_goods:
        print(*[f'id: {product["id"]} - {product["name"]}'
                for product in all_goods], sep='\n')
    else:
        print('No such goods.')


def get_specific_product(product_id: str, st_connector):
    all_goods = st_connector.get_storage_info()['Goods']
    if int(product_id) > len(all_goods):
        raise InvalidIdError('Incorrect id.')
    for product in all_goods:
        if product.get('id') == int(product_id):
            if int(product.get('quantity')) > 0:
                print(*[f'{key}: {value}' for key, value in product.items()],
                      'You can buy this product.', sep='\n')
            else:
                print(*[f'{key}: {value}' for key, value in product.items()],
                      "You couldn't buy this product.", sep='\n')


def make_order(id_quantity_list: str, st_connector, ord_connector):
    id_quantity_list = [[item for item in id_quantity.split()]
                        for id_quantity in id_quantity_list.split(',')]
    storage = st_connector.get_storage_info()
    goods_list = storage['Goods']
    order = {}
    for _id, quantity in id_quantity_list:
        if not _id.isdigit() or not quantity.isdigit():
            raise InvalidIdError('Product id and quantity '
                                 'of goods must be a digit.')
        elif int(_id) > len(goods_list):
            raise InvalidIdError('Incorrect product id.')
        for product in goods_list:
            if product['id'] == int(_id):
                if product['quantity'] >= int(quantity):
                    order[f'product_id: {_id}'] = int(quantity)
                    product['quantity'] -= int(quantity)
                    order['order price'] = (order.get('order price', 0)
                                            + float(product['price'])
                                            * int(quantity))
                    continue
                else:
                    return "it is not possible to deliver such order."
    if ord_connector.read_file():
        order['order id'] = len(ord_connector.get_order_info()) + 1
    else:
        order['order id'] = 1
    order['created_at'] = str(date.today())
    storage['Goods'] = goods_list
    st_connector.record_with_new_info(storage)
    ord_connector.record_order(order)
    result = {'total order price': order['order price']}
    for key in order:
        if 'product_id' in key:
            result[key] = order[key]
    return [f'{key}: {value}' for key, value in result.items()]


def get_categories_statistic(min_date, max_date, ct_connector,
                             ord_connector, st_connector):
    categories = ct_connector.get_all_categories().keys()
    sold_goods = get_sold_items(min_date, max_date,
                                ord_connector, st_connector)
    quantity = {}
    price = {}
    for category in categories:
        for key in sold_goods.keys():
            if category == key[1]:
                quantity[category] = (sold_goods[key]
                                      + quantity.get(category, 0))
                price[category] = (sold_goods[key] * float(key[2])
                                   + price.get(category, 0))
            else:
                quantity[category] = quantity.get(category, 0)
                price[category] = price.get(category, 0)
    return {"Category": categories,
            "Quantity": quantity.values(),
            "Total revenues": price.values()}


def get_sold_items(min_date, max_date, ord_connector, st_connector):
    orders = ord_connector.get_order_info()
    if min_date.strip():
        orders = list(filter(lambda x:
                             date.fromisoformat(x['created_at'])
                             >= date.fromisoformat(min_date), orders))
    if max_date.strip():
        orders = list(filter(lambda x:
                             date.fromisoformat(x['created_at'])
                             <= date.fromisoformat(max_date), orders))
    goods = {}
    for (id_, name,
         category, price) in map(lambda x: [x['id'], x['name'],
                                            x['category'], x['price']],
                                 st_connector.get_storage_info()['Goods']):
        for order in orders:
            if f'product_id: {id_}' in order.keys():
                goods[(name,
                       category, price)] = (goods.get((name,
                                                       category, price), 0)
                                            + order[f'product_id: {id_}'])
    return goods


def get_sorted_orders_list(min_date, max_date, ord_connector):
    orders = ord_connector.get_order_info()
    if min_date.strip():
        orders = filter(lambda x:
                        date.fromisoformat(x['created_at'])
                        >= date.fromisoformat(min_date), orders)
    if max_date.strip():
        orders = filter(lambda x:
                        date.fromisoformat(x['created_at'])
                        <= date.fromisoformat(max_date), orders)
    return sorted(orders, key=lambda x: x['order price'], reverse=True)


def get_common_info(min_date, max_date, ord_connector, st_connector):
    orders = ord_connector.get_order_info()
    if min_date.strip():
        orders = list(filter(lambda x:
                             date.fromisoformat(x['created_at'])
                             >= date.fromisoformat(min_date), orders))
    if max_date.strip():
        orders = list(filter(lambda x:
                             date.fromisoformat(x['created_at'])
                             <= date.fromisoformat(max_date), orders))
    total_revenues = sum(map(lambda x: x['order price'], orders))
    total_amount = len(get_sold_items(min_date, max_date,
                                      ord_connector, st_connector))
    products = get_sold_items(min_date, max_date,
                              ord_connector, st_connector).items()
    most_popular_products = sorted(products, key=lambda x: x[1])
    most_popular_product = most_popular_products[-1][0][0]
    most_popular_category = ''
    for item in st_connector.get_storage_info()['Goods']:
        if item['name'] == most_popular_product:
            most_popular_category = item['category']
    return {"Total revenues": total_revenues,
            "Total amount": total_amount,
            "The most popular category": most_popular_category,
            "The most popular product": most_popular_product}


def get_statistic(min_date, max_date, st_connector,
                  ord_connector, ct_connector):
    record_to_exel_sheets(get_categories_statistic(min_date, max_date,
                                                   ct_connector,
                                                   ord_connector,
                                                   st_connector),
                          get_sold_items(min_date, max_date,
                                         ord_connector, st_connector),
                          get_sorted_orders_list(min_date,
                                                 max_date, ord_connector),
                          get_common_info(min_date, max_date,
                                          ord_connector, st_connector))
