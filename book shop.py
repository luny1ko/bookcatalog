from classes import Book
from classes import Catalog

def add_new_book():
    title = input("Введите название книги: ")
    author = input("Введите автора книги: ")
    genre = input("Введите жанр книги: ")
    year = input("Введите год издания книги: ")

    return Book(title, author, genre, year)

def search_books(catalog):
    keyword = input("Введите ключевое слово для поиска: ")
    results = catalog.search_books(keyword)

    if results:
        print("\nРезультаты поиска:")
        print('Название | Автор | Жанр | Год')
        for book in results:
            print(book)
    else:
        print("Книг по заданному критерию не найдено.")

def remove_book(catalog):
    title = input("Введите название книги для удаления: ")
    catalog.remove_book(title)

def main():
    catalog = Catalog()

    while True:
        print("\nМеню:")
        print("1. Добавить новую книгу")
        print("2. Показать каталог книг")
        print("3. Удалить книгу")
        print("4. Найти книгу")
        print("5. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            new_book = add_new_book()
            catalog.add_book(new_book)
            print("Книга добавлена в каталог.")
        elif choice == '2':
            catalog.show_catalog()
        elif choice == '3':
            remove_book(catalog)
        elif choice == '4':
            search_books(catalog)
        elif choice == '5':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()