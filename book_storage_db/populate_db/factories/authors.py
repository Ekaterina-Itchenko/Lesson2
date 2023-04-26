from __future__ import annotations
from typing import TYPE_CHECKING
from data_access.dto import AuthorsDTO
if TYPE_CHECKING:
    from ..fake_lib import (NameProvider,
                            LastNameProvider,
                            DateProvider,
                            TextProvider)


class AuthorsFactory:
    def __init__(
            self,
            first_name: NameProvider,
            last_name: LastNameProvider,
            birth_date: DateProvider,
            death_date: DateProvider,
            information: TextProvider
    ) -> None:
        self._first_name = first_name
        self._last_name = last_name
        self._birth_date = birth_date
        self._death_date = death_date
        self._information = information

    def generate(self) -> AuthorsDTO:
        random_date = self._birth_date()
        return AuthorsDTO(first_name=self._first_name(),
                          last_name=self._last_name(),
                          birth_date=random_date,
                          death_date=self._death_date(random_date),
                          information=self._information())
