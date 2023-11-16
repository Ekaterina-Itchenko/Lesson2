from typing import Protocol, TYPE_CHECKING
if TYPE_CHECKING:
    from data_access import StorageInfo, OrderInfo, CategoryInfo
    from DTO import OrderDTO


class StorageProto(Protocol):
    def get_storage_info(self) -> 'StorageInfo':
        raise NotImplementedError

    def record_with_new_info(self, new_info: 'StorageInfo') -> None:
        raise NotImplementedError


class CategoriesProto(Protocol):
    def get_all_categories(self) -> 'CategoryInfo':
        raise NotImplementedError

    def record_new_category(self,
                            category: str,
                            parameters: list[str]) -> None:
        raise NotImplementedError


class OrdersProto(Protocol):
    def get_order_info(self) -> 'OrderInfo':
        raise NotImplementedError

    def record_order(self,
                     order: 'OrderDTO') -> None:
        raise NotImplementedError

    def read_file(self) -> bool:
        raise NotImplementedError
