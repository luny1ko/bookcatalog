# main.py

from classes import Task, TaskList


def add_new_task():
    name = input("Введите название задачи: ")
    description = input("Введите описание задачи: ")
    priority = input("Введите приоритет задачи: ")
    return Task(description, priority, name)


def remove_task(catalog):
    task_name = input("Введите название задачи, которую хотите удалить: ")
    catalog.remove_task(task_name)


def search_task(catalog):
    task_name = input("Введите название задачи для поиска: ")
    catalog.search_task(task_name)


def modify_task(catalog):
    print("\nСписок задач для изменения:")
    catalog.show_list()

    try:
        task_index = int(input("\nВведите номер задачи, которую хотите изменить: ")) - 1
        task = catalog.get_task_by_index(task_index)

        if task:
            print(f"\nВы выбрали задачу: {task}")
            action = input("Что вы хотите изменить? (1 - Описание, 2 - Приоритет): ")

            if action == "1":
                new_description = input("Введите новое описание задачи: ")
                task.update_description(new_description)
                print("Описание обновлено!")

            elif action == "2":
                new_priority = input("Введите новый приоритет задачи (Высокий, Средний, Низкий): ")
                task.update_priority(new_priority)
                print("Приоритет обновлен!")

            else:
                print("Неверный выбор.")
        else:
            print("Задача с таким номером не найдена.")
    except ValueError:
        print("Ошибка: введите правильный номер задачи.")


def main():
    task_list = TaskList()

    while True:
        print("\nМеню:")
        print("1. Добавить новую задачу")
        print("2. Показать список задач")
        print("3. Удалить задачу")
        print("4. Найти задачу")
        print("5. Изменить задачу")
        print("6. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            new_task = add_new_task()
            task_list.add_task(new_task)
            print("Задача добавлена в список.")
        elif choice == '2':
            task_list.show_list()
        elif choice == '3':
            remove_task(task_list)
        elif choice == '4':
            search_task(task_list)
        elif choice == '5':
            modify_task(task_list)
        elif choice == '6':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
