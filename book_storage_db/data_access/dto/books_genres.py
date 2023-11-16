from dataclasses import dataclass


@dataclass
class BooksGenresDTO:
    book_id: int
    genre_id: int
