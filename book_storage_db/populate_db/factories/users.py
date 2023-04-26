from __future__ import annotations
from typing import TYPE_CHECKING
from data_access.dto import UsersDTO
if TYPE_CHECKING:
    from ..fake_lib import (NameProvider,
                            LastNameProvider,
                            DigitProvider,
                            EmailProvider,
                            PhoneProvider,
                            PasswordProvider)


class UsersFactory:
    def __init__(
            self,
            first_name: NameProvider,
            last_name: LastNameProvider,
            user_name: NameProvider,
            age: DigitProvider,
            email: EmailProvider,
            phone_number: PhoneProvider,
            password: PasswordProvider
    ) -> None:
        self._first_name = first_name
        self._last_name = last_name
        self._user_name = user_name
        self._age = age
        self._email = email
        self._phone_number = phone_number
        self._password = password

    def generate(self) -> UsersDTO:
        return UsersDTO(first_name=self._first_name(),
                        last_name=self._last_name(),
                        user_name=self._user_name(),
                        age=self._age(),
                        email=self._email(),
                        phone_number=self._phone_number(),
                        password=self._password())
