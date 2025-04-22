from classes import Book
from classes import Catalog

def add_new_book():
    title = input("Введите название книги: ")
    author = input("Введите автора книги: ")
    genre = input("Введите жанр книги: ")
    year = input("Введите год издания книги: ")


    new_book = Book(title, author, genre, year)
    return new_book


def main():
    catalog = Catalog()

    while True:
        print("\nМеню:")
        print("1. Добавить новую книгу")
        print("2. Показать каталог книг")
        print("3. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            new_book = add_new_book()
            catalog.add_book(new_book)
            print("Книга добавлена в каталог.")
        elif choice == '2':
            print("\nКаталог книг:")
            catalog.show_catalog()
        elif choice == '3':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()