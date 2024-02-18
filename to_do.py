class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("\nTask added successfully.")

    def view_tasks(self):
        if self.tasks:
            print("\nTasks:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("\nNo tasks added yet.")

    def complete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks.pop(task_index - 1)
            print(f"\nCompleted task: '{task}'")
        else:
            print("\nInvalid task index.")

    def delete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks.pop(task_index - 1)
            print(f"\nDeleted task: '{task}'")
        else:
            print("\nInvalid task index.")


def main():
    todo_list = TodoList()

    while True:
        print("\nTodo List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            task = input("\nEnter task to add: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            task_index = int(input("\nEnter index of task to mark as completed: "))
            todo_list.complete_task(task_index)
        elif choice == "4":
            task_index = int(input("\nEnter index of task to delete: "))
            todo_list.delete_task(task_index)
        elif choice == "5":
            print("\nExiting Todo List. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please choose again.")


if __name__ == "__main__":
    main()
