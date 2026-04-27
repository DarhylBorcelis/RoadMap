import json
import sys
import os
from datetime import datetime

FILE = "tasks.json"


def load_tasks():
    if not os.path.exists(FILE):
        return []
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []


def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)


def generate_id(tasks):
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1


def add_task(description):
    tasks = load_tasks()

    new_task = {
        "id": generate_id(tasks),
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }

    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_task['id']})")


def update_task(task_id, description):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = description
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print("Task updated")
            return
    print("Task not found")


def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [t for t in tasks if t["id"] != task_id]
    if len(new_tasks) == len(tasks):
        print("Task not found")
        return

    save_tasks(new_tasks)
    print("Task deleted")


def mark_task(task_id, status):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task marked as {status}")
            return

    print("Task not found")


def list_tasks(filter_status=None):
    tasks = load_tasks()

    if filter_status:
        tasks = [t for t in tasks if t["status"] == filter_status]
    if not tasks:
        print("No tasks found")
        return
    for t in tasks:
        print(f"[{t['id']}] {t['description']} ({t['status']})")


def main():
    args = sys.argv
    if len(args) < 2:
        print("Usage: task-cli <command>")
        return
    
    command = args[1].lower()

    if command == "add":
        add_task(args[2])
    elif command == "update":
        update_task(int(args[2]), args[3])
    elif command == "delete":
        delete_task(int(args[2]))
    elif command == "mark-done":
        mark_task(int(args[2]), "done")
    elif command == "mark-in-progress":
        mark_task(int(args[2]), "in-progress")
    elif command == "list":
        if len(args) > 2:
            list_tasks(args[2])
        else:
            list_tasks()
    else:
        print("Unknown command")


if __name__ == "__main__":
    main()