import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a task")
input_box = sg.InputText(tooltip="Enter task", key="task")

add_botton = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_tasks(), key="tasks", enable_events=True, size=[45, 10])

edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")

exit_button = sg.Button("Exit")

window = sg.Window("My Tasks App", layout=[[label, input_box, add_botton],
                                           [list_box, edit_button, complete_button], [exit_button]], font=("Helvetica", 15))

while True:
    event, values = window.read()
    print(event)
    print(values)

    match event:
        case "Add":
            tasks = functions.get_tasks()
            new_task = values["task"] + "\n"
            tasks.append(new_task)
            functions.write_tasks(tasks)
            window["tasks"].update(values=tasks)
        case "Edit":
            task_to_edit = values["tasks"][0]
            new_task = values["task"]

            tasks = functions.get_tasks()
            index = tasks.index(task_to_edit)
            tasks[index] = new_task

            functions.write_tasks(tasks)
            window["tasks"].update(values=tasks)
        case "tasks":
            window["task"].update(value=values["tasks"][0])
        case "Complete":
            task_to_complete = values["tasks"][0]
            tasks = functions.get_tasks()
            tasks.remove(task_to_complete)
            functions.write_tasks(tasks)

            window["tasks"].update(values=tasks)
            window["task"].update(value="")

        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

window.close()