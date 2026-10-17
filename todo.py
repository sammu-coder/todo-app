# Simple Todo App by Sammu Coder
tasks = []

while True:
    print("\n1. Add Task  2. View Tasks  3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        print("\nYour Tasks:")
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")

    elif choice == "3":
        print("Bye!")
        break
