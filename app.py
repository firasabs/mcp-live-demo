import argparse
import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("tasks.json")


def load_tasks():
    if not DATA_FILE.exists():
        return []

    with DATA_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


def save_tasks(tasks):
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2)


def list_tasks():
    tasks = load_tasks()

    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        status = "x" if task["completed"] else " "
        print(f"[{status}] {task['id']}. {task['title']}")


def add_task(title):
    tasks = load_tasks()
    next_id = max((task["id"] for task in tasks), default=0) + 1

    task = {
        "id": next_id,
        "title": title,
        "completed": False,
    }

    tasks.append(task)
    save_tasks(tasks)

    print(f"Added task {next_id}: {title}")


def complete_task(task_id):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            save_tasks(tasks)
            print(f"Completed task {task_id}.")
            return

    print(f"Task {task_id} was not found.")


def main():
    parser = argparse.ArgumentParser(description="Simple command-line task manager")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("list", help="List all tasks")

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", help="Task title")

    complete_parser = subparsers.add_parser("complete", help="Mark a task as completed")
    complete_parser.add_argument("task_id", type=int, help="Task ID")

    args = parser.parse_args()

    if args.command == "list":
        list_tasks()
    elif args.command == "add":
        add_task(args.title)
    elif args.command == "complete":
        complete_task(args.task_id)


if __name__ == "__main__":
    main()
