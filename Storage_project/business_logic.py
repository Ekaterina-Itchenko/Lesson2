from data_access import (record_to_exel_sheets,
                         CommonInfoDTO,
                         CategoryStatisticDTO)
from errors import (CategoryExistenceError,
                    InvalidCategoryError,
                    InvalidIdError)
from datetime import date
from typing import TYPE_CHECKING
from DTO import StorageDTO, OrderDTO
if TYPE_CHECKING:
    from interfaces import StorageProto, CategoriesProto, OrdersProto
    from data_access import OrderInfo


def add_category(category: str,
                 parameters: str,
                 ct_connector: 'CategoriesProto') -> None:
    for item in ct_connector.get_all_categories():
        if item.category.lower() == category.lower():
            raise CategoryExistenceError("This category has already exists.")
    parameters_list = [element.strip().lower() for
                       element in parameters.split(',')]
    if 'price' not in parameters_list:
        parameters_list.append('price')
    if 'name' not in parameters_list:
        parameters_list.append('name')
    ct_connector.record_new_category(category, parameters_list)


def get_parameters(category: str,
                   ct_connector:
                   'CategoriesProto') -> list[str] | None:
    if category.lower() not in [item.category.lower()
                                for item in
                                ct_connector.get_all_categories()]:
        raise InvalidCategoryError("This category is not exist.")
    for item in ct_connector.get_all_categories():
        if category.lower() == item.category.lower():
            return item.parameters
    return None


def add_new_goods(info: dict[str, str], amount_of_goods: str,
                  category: str, st_connector: 'StorageProto') -> None:
    info['category'] = category
    goods_list = st_connector.get_storage_info()
    flag = True
    for product in goods_list:
        products_set = set((("id", product.id),
                            ("name", product.name),
                            ("price", product.price),
                            ("category", product.category)))
        if set(info.items()).issubset(products_set):
            product.quantity += int(amount_of_goods)
            product.updated_at = str(date.today())
            st_connector.record_with_new_info(goods_list)
            flag = False

    if flag:
        add_param = {}
        for key in info:
            if key not in list(StorageDTO.__dict__['__annotations__'].keys()):
                add_param[key] = info[key]

        new_info = StorageDTO(category=category,
                              quantity=int(amount_of_goods),
                              created_at=str(date.today()),
                              updated_at=str(date.today()),
                              product_id=len(goods_list) + 1,
                              name=info['name'],
                              price=info["price"],
                              add_param=add_param)

        goods_list.append(new_info)
        st_connector.record_with_new_info(goods_list)


def get_info_of_goods(category: str,
                      min_date: str,
                      max_date: str,
                      st_connector: 'StorageProto',
                      ct_connector: 'CategoriesProto') -> None:
    all_goods = st_connector.get_storage_info()
    if category.strip():
        if (category.lower() not in
                [item.category.lower() for item in
                 ct_connector.get_all_categories()]):
            raise InvalidCategoryError("This category is not exist.")
        result = []
        for product in all_goods:
            if product.category.lower() == category.lower():
                result.append(product)
        all_goods = result
    if min_date.strip():
        result = []
        for product in all_goods:
            if (date.fromisoformat(product.created_at) >=
                    date.fromisoformat(min_date.strip())):
                result.append(product)
        all_goods = result
    if max_date.strip():
        result = []
        for product in all_goods:
            if (date.fromisoformat(product.created_at) <=
                    date.fromisoformat(max_date.strip())):
                result.append(product)
        all_goods = result
    if all_goods:
        print(*[f'id: {product.id} - {product.name}'
                for product in all_goods], sep='\n')
    else:
        print('No such goods.')


def get_specific_product(product_id: str,
                         st_connector: 'StorageProto') -> None:
    all_goods = st_connector.get_storage_info()
    if int(product_id) > len(all_goods):
        raise InvalidIdError('Incorrect id.')
    for product in all_goods:
        if product.product_id == int(product_id):
            info = {'name': product.name,
                    "id": product.product_id,
                    "category": product.category,
                    "created_at": product.created_at,
                    "price": product.price,
                    "quantity": product.quantity}
            if int(product.quantity) > 0:
                print(*[f'{key}: {value}' for key, value in info.items()],
                      'You can buy this product.', sep='\n')
            else:
                print(*[f'{key}: {value}' for key, value in info.items()],
                      "You couldn't buy this product.", sep='\n')


def make_order(id_quantity: str,
               st_connector: 'StorageProto',
               ord_connector: 'OrdersProto') -> list[str] | str:
    id_quantity_list = [id_quant.split()
                        for id_quant in id_quantity.split(',')]
    goods_list = st_connector.get_storage_info()

    order_goods = []
    order_price = []
    for _id, quantity in id_quantity_list:
        if not _id.isdigit() or not quantity.isdigit():
            raise InvalidIdError('Product id and quantity '
                                 'of goods must be a digit.')
        elif int(_id) > len(goods_list):
            raise InvalidIdError('Incorrect product id.')
        for product in goods_list:
            if product.product_id == int(_id):
                if product.quantity >= int(quantity):
                    order_goods.append({"product_id": int(_id),
                                        "quantity": int(quantity)})
                    product.quantity -= int(quantity)
                    order_price.append(float(product.price) * int(quantity))
                    continue
                else:
                    return "it is not possible to deliver such order."
    if ord_connector.read_file():
        order_id = len(ord_connector.get_order_info()) + 1
    else:
        order_id = 1

    order = OrderDTO(order_id=order_id,
                     goods=order_goods,
                     order_price=sum(order_price),
                     created_at=str(date.today()))

    st_connector.record_with_new_info(goods_list)
    ord_connector.record_order(order)
    return [f"order id: {order.order_id}", f"List of goods: {order.goods}",
            f"Order price: {order.order_price}",
            f"Created date: {order.created_at}"]


def get_categories_statistic(min_date: str,
                             max_date: str,
                             ct_connector: 'CategoriesProto',
                             ord_connector: 'OrdersProto',
                             st_connector: 'StorageProto') \
        -> 'CategoryStatisticDTO':
    categories = ct_connector.get_all_categories()
    sold_goods = get_sold_items(min_date, max_date,
                                ord_connector, st_connector)
    quantity: dict[str, int] = {}
    price: dict[str, float] = {}
    for category in categories:
        for key in sold_goods:
            if category.category == key[1]:
                quantity[key[1]] = (sold_goods[key]
                                    + quantity.get(key[1], 0))
                price[key[1]] = (sold_goods[key] * float(key[2])
                                 + price.get(key[1], 0))
            else:
                quantity[category.category] = \
                    quantity.get(category.category, 0)
                price[category.category] = price.get(category.category, 0)
    return CategoryStatisticDTO(category=list(quantity.keys()),
                                quantity=list(quantity.values()),
                                total_revenues=list(price.values()))


def get_sold_items(min_date: str,
                   max_date: str,
                   ord_connector: 'OrdersProto',
                   st_connector: 'StorageProto') -> dict[tuple[str,
                                                               str,
                                                               str], int]:
    orders = ord_connector.get_order_info()
    if min_date.strip():
        orders = list(filter(lambda x:
                             date.fromisoformat(x.created_at)
                             >= date.fromisoformat(min_date), orders))
    if max_date.strip():
        orders = list(filter(lambda x:
                             date.fromisoformat(x.created_at)
                             <= date.fromisoformat(max_date), orders))
    goods: dict[tuple[str, str, str], int] = {}
    for (id_, name,
         category, price) in map(lambda x: [x.id, x.name,
                                            x.category, x.price],
                                 st_connector.get_storage_info()):
        for order in orders:
            for item in order.goods:
                if id_ == item["product_id"]:
                    goods[(str(name),
                           str(category),
                           str(price))] = (goods.get((str(name),
                                                      str(category),
                                                      str(price)), 0)
                                           + item["quantity"])
    return goods


def get_sorted_orders_list(min_date: str,
                           max_date: str,
                           ord_connector: 'OrdersProto') -> 'OrderInfo':
    orders = ord_connector.get_order_info()
    if min_date.strip():
        orders = list(filter(lambda x:
                             date.fromisoformat(x.created_at)
                             >= date.fromisoformat(min_date), orders))
    if max_date.strip():
        orders = list(filter(lambda x:
                             date.fromisoformat(x.created_at)
                             <= date.fromisoformat(max_date), orders))
    return sorted(orders, key=lambda x: x.order_price, reverse=True)


def get_common_info(min_date: str,
                    max_date: str,
                    ord_connector: 'OrdersProto',
                    st_connector: 'StorageProto') -> 'CommonInfoDTO':
    orders = ord_connector.get_order_info()
    if min_date.strip():
        orders = list(filter(lambda x:
                             date.fromisoformat(x.created_at)
                             >= date.fromisoformat(min_date), orders))
    if max_date.strip():
        orders = list(filter(lambda x:
                             date.fromisoformat(x.created_at)
                             <= date.fromisoformat(max_date), orders))
    total_revenues = sum(map(lambda x: x.order_price, orders))
    total_amount = len(get_sold_items(min_date, max_date,
                                      ord_connector, st_connector))
    products = get_sold_items(min_date, max_date,
                              ord_connector, st_connector).items()
    most_popular_products = sorted(products, key=lambda x: x[1])
    most_popular_product = most_popular_products[-1][0][0]
    most_popular_category: str = ''
    for item in st_connector.get_storage_info():
        if item.name == most_popular_product:
            most_popular_category = item.category
    return CommonInfoDTO(total_revenues=total_revenues,
                         total_amount=total_amount,
                         popular_category=most_popular_category,
                         popular_product=most_popular_product)


def get_statistic(min_date: str,
                  max_date: str,
                  st_connector: 'StorageProto',
                  ord_connector: 'OrdersProto',
                  ct_connector: 'CategoriesProto') -> None:

    info1 = get_categories_statistic(min_date,
                                     max_date,
                                     ct_connector,
                                     ord_connector,
                                     st_connector)

    info2 = get_sold_items(min_date,
                           max_date,
                           ord_connector,
                           st_connector)
    info3 = get_sorted_orders_list(min_date,
                                   max_date,
                                   ord_connector)

    info4 = get_common_info(min_date,
                            max_date,
                            ord_connector,
                            st_connector)
    record_to_exel_sheets(info1, info2, info3, info4)
