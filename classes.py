class Book:
    def __init__(self, title, author, genre, year):
        self.title = title
        self.author = author
        self.genre = genre
        self.year = year

    def __str__(self):
        print('Название | Автор | Жанр | Год')
        return f"{self.title} | {self.author} | {self.genre} | {self.year}"

class Catalog:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_catalog(self):
        if not self.books:
            print("Каталог пуст.")
        else:
            for book in self.books:
                print(book)