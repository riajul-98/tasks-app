import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a task")
input_box = sg.InputText(tooltip="Enter task", key="task")
add_botton = sg.Button("Add")

window = sg.Window("My Tasks App", layout=[[label, input_box, add_botton]], font=("Helvetica", 20))

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
        case sg.WIN_CLOSED:
            break

window.close()