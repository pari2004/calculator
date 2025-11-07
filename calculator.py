# ...existing code...

def calculator():
    print("\nSimple Calculator")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Select operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        op = input("Choose an operation (1/2/3/4): ")

        if op == '1':
            result = num1 + num2
            print(f"Result: {num1} + {num2} = {result}")
        elif op == '2':
            result = num1 - num2
            print(f"Result: {num1} - {num2} = {result}")
        elif op == '3':
            result = num1 * num2
            print(f"Result: {num1} * {num2} = {result}")
        elif op == '4':
            if num2 == 0:
                print("Error: Division by zero.")
            else:
                result = num1 / num2
                print(f"Result: {num1} / {num2} = {result}")
        else:
            print("Invalid operation choice.")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

def main():
    storage = TaskStorage()  # Create a storage instance
    task_controller = TaskController(storage)  # Pass storage to controller

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Update Task")
        print("3. View Tasks")
        print("4. Calculator")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            task_controller.add_task(title, description)
            print("Task added successfully.")

        elif choice == '2':
            task_id = input("Enter task ID to update: ")
            new_status = input("Enter new status (completed/incomplete): ")
            task_controller.update_task(task_id, new_status)
            print("Task updated successfully.")

        elif choice == '3':
            tasks = task_controller.get_tasks()
            for task in tasks:
                print(f"ID: {task.id}, Title: {task.title}, Status: {task.status}")

        elif choice == '4':
            calculator()

        elif choice == '5':
            print("Exiting the application.")
            sys.exit()

        else:
            print("Invalid option. Please try again.")