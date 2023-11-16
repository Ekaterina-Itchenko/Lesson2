from __future__ import annotations
from typing import TYPE_CHECKING
from data_access.dto import GenresDTO
if TYPE_CHECKING:
    from ..fake_lib import GenreProvider, TextProvider


class GenresFactory:
    def __init__(
            self,
            genre_name: GenreProvider,
            genre_description: TextProvider
    ) -> None:
        self._genre_name = genre_name
        self._genre_description = genre_description

    def generate(self) -> GenresDTO:
        return GenresDTO(genre_name=self._genre_name(),
                         description=self._genre_description())
