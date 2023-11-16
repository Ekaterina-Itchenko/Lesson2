from typing import Protocol, TYPE_CHECKING
if TYPE_CHECKING:
    from data_access import CompaniesInfo
    from DTO import CompanyDTO


class DbProto(Protocol):
    def get_file_information(self) -> 'CompaniesInfo':
        raise NotImplementedError

    def record_new_line(self, new_line: 'CompanyDTO') -> None:
        raise NotImplementedError

    def record_new_information(self,
                               new_information: 'CompaniesInfo') -> None:
        raise NotImplementedError
