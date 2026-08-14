# To-Do List – Project Report

## 1. Objective

The objective of this project is to create a simple command-line To-Do List application that allows users to add, delete, and view tasks.

## 2. Methodology

The program uses a Python list to store tasks. A continuous `while` loop displays a menu and allows the user to select an action.

The application provides four options:

* **Add Task** – Adds a new task to the list.
* **Delete Task** – Removes a selected task using its task number.
* **View Tasks** – Displays all currently stored tasks.
* **Exit** – Closes the program.

## 3. Implementation

The `tasks` list stores all entered tasks. The `append()` method is used to add tasks, while `pop()` removes a selected task.

Conditional statements are used to process the user's menu choice, and a `for` loop displays the tasks with numbered positions. The program also checks whether the task list is empty before displaying or deleting tasks.

## 4. Testing and Results

The program was tested by adding multiple tasks, viewing the task list, deleting selected tasks, and exiting the application.

It also correctly handles an empty task list and invalid menu or task numbers by displaying appropriate messages.

## 5. Conclusion

The To-Do List application successfully provides basic task management through a simple command-line interface. The project demonstrates the use of Python lists, loops, conditional statements, user input, and basic list operations.
