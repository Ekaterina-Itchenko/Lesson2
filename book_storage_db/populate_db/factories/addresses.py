from __future__ import annotations
from typing import TYPE_CHECKING
from data_access.dto import AddressesDTO
if TYPE_CHECKING:
    from ..fake_lib import (CountryProvider,
                            DigitProvider,
                            CityProvider,
                            WordProvider)


class AddressesFactory:
    def __init__(
            self,
            country: CountryProvider,
            city: CityProvider,
            street: WordProvider,
            home_number: DigitProvider,
            post_code: DigitProvider
    ) -> None:
        self._country = country
        self._city = city
        self._street = street
        self._home_number = home_number
        self._post_code = post_code

    def generate(self) -> AddressesDTO:
        random_country = self._country()
        return AddressesDTO(country=random_country,
                            city=self._city(random_country),
                            street=self._street(),
                            home_number=self._home_number(),
                            post_code=self._post_code())
