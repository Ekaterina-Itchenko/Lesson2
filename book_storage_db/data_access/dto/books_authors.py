from dataclasses import dataclass


@dataclass
class BooksAuthorsDTO:
    book_id: int
    author_id: int
