class Book:
    def __init__(self, title, author, genre, year):
        self.title = title
        self.author = author
        self.genre = genre
        self.year = year

    def __str__(self):
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

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f"Книга '{book.title}' удалена из каталога.")
                return
        print("Книга не найдена.")

    def search_books(self, keyword):
        results = []
        for book in self.books:
            if (keyword.lower() in book.title.lower() or
                    keyword.lower() in book.author.lower() or
                    keyword.lower() in book.genre.lower() or
                    keyword.lower() in book.year.lower()):
                results.append(book)
        return results