# task.py
#
# [x] add a task
# [x] delete a task
# [x] show a list of all tasks
# [x] store it in a file

import json

tasks = []

def save_tasks(tasks):
    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(tasks, file)

def clear_tasks(tasks):
    if not tasks:
        raise Exception("No tasks to clear.")

    if input("Are you sure? Type 'clear' to confirm. ") == "clear":
        tasks.clear()
        save_tasks(tasks)
        print("All tasks cleared successfully!")
    else:
        print("Aborted.")

def show_tasks(tasks):
    if tasks:
        print("-" * 30)

        for index, task in enumerate(tasks):
            print(f"{index + 1} - " + task)

        print("-" * 30)
    else:
        print("No tasks.")


def delete_task(tasks):
    if tasks:
        user_input = input("Enter the task to delete: ")

    if user_input.isdigit():
        task_num = int(user_input)
        if 0 < task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Task '{removed}' removed successfully.")
        else:
            print("Invalid number.")
    else:
        if user_input in tasks:
            tasks.remove(user_input)
            save_tasks(tasks)
            print(f"Task '{user_input}' removed successfully.")
        else:
            print("Invalid task.")


def add_task(tasks):
    task = input("Enter the task: ")

    if task in tasks:
        print("This task is already on the list.")
    elif task.isdigit():
        print("Task can't be a number.")
    else:
        tasks.append(task)
        save_tasks(tasks)


def main():
    try:
        with open("tasks.json", "r", encoding="utf-8") as file:
            tasks = json.load(file)
            print("file found. restored.")
    except (FileNotFoundError, json.JSONDecodeError):
        print("no tasks found, or the file is corrupted. fresh start.")
        tasks = []

    while True:
        print("1. Add a task")
        print("2. Delete a task")
        print("3. Show all tasks")
        print("0. Clear all tasks.")
        print()
        print("'q' to exit.")
        choice = input()

        match choice:
            case "1":
                add_task(tasks)
            case "2":
                delete_task(tasks)
            case "3":
                show_tasks(tasks)
            case "0":
                try:
                    clear_tasks(tasks)
                except Exception as e:
                    print(e)
            case "q":
                return 0
            case _:
                print("You were close.")
                continue


if __name__ == "__main__":
    main()
