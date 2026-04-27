# Task Tracker CLI

A simple command-line interface (CLI) application to manage your tasks. This project tracks tasks, their statuses, and timestamps using a local JSON file.

## Requirements

The application runs from the command line, accepts user actions and inputs as arguments, and stores the tasks in a JSON file. The user is able to:

* **Add, Update, and Delete** tasks
* **Mark a task** as in progress or done
* **List all tasks**
* **List tasks by status** (done, todo, or in-progress)

## Implementation Constraints

* **No External Libraries:** Built using only the native modules of the chosen programming language.
* **Storage:** Data is persisted in a `tasks.json` file in the current directory.
* **Auto-initialization:** The JSON file is automatically created if it does not exist.
* **Arguments:** Uses positional command-line arguments for user inputs.
* **Error Handling:** Graceful handling of edge cases and invalid inputs.

## Usage Examples

Below are the commands and their expected usage:

```bash
# Adding a new task
task-cli add "Buy groceries"
# Output: Task added successfully (ID: 1)

# Updating and deleting tasks
task-cli update 1 "Buy groceries and cook dinner"
task-cli delete 1

# Marking a task as in progress or done
task-cli mark-in-progress 1
task-cli mark-done 1

# Listing all tasks
task-cli list

# Listing tasks by status
task-cli list done
task-cli list todo
task-cli list in-progress
```

## Task Properties

Each task is stored as an object with the following properties:

| Property | Description |
| :--- | :--- |
| `id` | A unique identifier for the task |
| `description` | A short description of the task |
| `status` | The status of the task (`todo`, `in-progress`, `done`) |
| `createdAt` | The date and time when the task was created |
| `updatedAt` | The date and time when the task was last updated |

---