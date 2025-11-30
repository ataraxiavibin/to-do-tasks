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
    if input("Are you sure? Type 'clear' to confirm. ") == "clear":
        tasks.clear()
        save_tasks(tasks)
        print("All tasks cleared successfully!")
    else:
        print("Aborted.")

def show_tasks(tasks):
    if tasks:
        print("-" * 30)

        for task in tasks:
            print("- " + task)

        print("-" * 30)
    else:
        print("No tasks.")


def delete_task(tasks):
    task = input("Enter the task to delete: ")

    if task in tasks:
        tasks.remove(task)
        print(f"Task {task} removed successfully.")
        save_tasks(tasks)
    else:
        print("There is no task to remove.")


def add_task(tasks):
    task = input("Enter the task: ")   

    if task not in tasks:
        tasks.append(task)
        save_tasks(tasks)
    else:
        print("This task is already on the list.")


def main():
    try:
        with open("tasks.json", "r", encoding="utf-8") as file:
            print("file found. restored.")
            tasks = json.load(file)
    except FileNotFoundError:
        print("dry run.")
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
                clear_tasks(tasks)
            case "q":
                return 0
            case _:
                print("You were close.")
                continue


if __name__ == "__main__":
    main()
