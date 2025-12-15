from functions import get_tasks, write_tasks
import time

current_time = time.strftime("%d %b %Y %H:%M:%S")
print(f"It is currently {current_time}")


while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    if user_action.startswith("add"):
        task = user_action[4:]

        tasks = get_tasks()

        tasks.append(task + "\n")

        write_tasks(tasks)

    elif user_action.startswith("show"):

        tasks = get_tasks()

        for index, item in enumerate(tasks):
            item = item.strip("\n")
            print(f"{index + 1}. {item}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number -= 1
            tasks = get_tasks()

            new_task = input("What would you like to replace this task with: ")
            tasks[number] = new_task + "\n"

            write_tasks(tasks)
        except ValueError:
            print("Your command is invalid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            tasks = get_tasks()

            removed_task = tasks[number - 1].strip("\n")
            tasks.pop(number - 1)

            write_tasks(tasks)

            message = f"Task {removed_task} has been removed from list"
            print(message)
        except IndexError:
            print("Please enter a valid number.")
            continue


    elif user_action.startswith("exit"):
        break

    else:
        print("Invalid command")

print("Bye!")