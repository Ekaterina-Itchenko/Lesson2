from functools import total_ordering
from errors import EmptyLibraryError


@total_ordering
class Book:

    def __init__(self, name, description, pages, author, price):
        self.name = name
        self.description = description
        self. pages = pages
        self. author = author
        self.price = price

    def to_dict(self):
        return self.__dict__

    def contains_word(self, word):
        name_words = [i.strip(',.?!&:()') for i in self.name.lower().split()]
        description_words = [i.strip(',.?!&:()') for i in
                             self.description.lower().split()]
        if word.lower() in name_words or word.lower() in description_words:
            return True
        else:
            return False

    def __gt__(self, other):
        return self.pages > other.pages

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return self.__dict__ != other.__dict__


class Library():
    def __init__(self):
        self.__books = {}

    @property
    def books(self):
        return self.__books

    def add_book(self, book):
        self.books[book.name] = book.__dict__
        print('Book has added')

    def get_books(self):
        return self.books.values()

    def remove_book(self, book):
        del self.books[book.name]

    def find_the_biggest_book(self):
        try:
            if self.books:
                return sorted(self.get_books(), key=lambda x: x['pages'])[-1]
            else:
                raise EmptyLibraryError('Book is not in the library')
        except EmptyLibraryError as err:
            return err


book1 = Book("1984", "Some description", 1500, "Orwell", 10)
book2 = Book("Learn Python",
             "This book will teach you how to learn python",
             1000,
             "Luhts", 49)
l1 = Library()
print(l1.books)
l1.add_book(book1)
print(l1.books)
l1.add_book(book2)
print(l1.books)
print(l1.get_books())
l1.remove_book(book1)
print(l1.books)
l1.remove_book(book2)
print(l1.find_the_biggest_book())
print(book1.contains_word('ggg'))
print(book2.to_dict())
print(book1 <= book2)
print(book1 != book2)
