

class Task:
    def __init__(self, description, priority, name):
        self.description = description
        self.priority = priority
        self.name = name

    def __str__(self):
        return f"Задача: {self.name} | Описание: {self.description} | Приоритет: {self.priority}"

    def update_description(self, new_description):
        self.description = new_description

    def update_priority(self, new_priority):
        self.priority = new_priority


class TaskList:
    PRIORITY_MAP = {"Высокий": 3, "Средний": 2, "Низкий": 1}
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def show_list(self):
        if not self.tasks:
            print("Список задач пуст.")
        else:
            self.tasks.sort(key=lambda x: self.PRIORITY_MAP[x.priority], reverse=True)
            for index, task in enumerate(self.tasks, 1):
                print(f"{index}. {task}")

    def get_task_by_index(self, index):
        if 0 <= index < len(self.tasks):
            return self.tasks[index]
        return None

    def search_task(self, task_name):
        found_tasks = [task for task in self.tasks if task_name.lower() in task.name.lower()]
        if found_tasks:
            print("Найденные задачи:")
            for task in found_tasks:
                print(task)
        else:
            print(f"Задача с именем '{task_name}' не найдена.")
