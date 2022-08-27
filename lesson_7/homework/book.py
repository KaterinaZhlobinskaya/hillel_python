from tkinter.messagebox import showinfo


class Book:
    def __init__(self, name, year, edition, genre, author, price):
        self.__name = name
        self.__year = year
        self.__edition = edition
        self.__genre = genre
        self.__author = author
        self.__price = price

    def show_info(self):
        print(f"the book {self.__name} published in {self.__year} by {self.__edition}, written in "
              f"{self.__genre} genre by {self.__author} costs {self.__price}$")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name = name

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        self.__year = year

    @property
    def edition(self):
        return self.__edition

    @edition.setter
    def edition(self, edition):
        self.__edition = edition

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, genre):
        self.__genre = genre

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author):
        self.__author = author

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price
house = Book (
    name="The House if the Seven Gables",
    year=2021,
    edition="Folio Publishing House",
    genre="a Ghotic novel",
    author="the American writer Nathaniel Hawthorne",
    price=3
)

gatsby = Book (
    name="The Great Gatsby",
    year=1925,
    edition=" Scribner's",
    genre="romantic",
    author="Francis Scott Key Fitzgerald",
    price=5
)

house.show_info()
gatsby.show_info()