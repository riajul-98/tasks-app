import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a task")
input_box = sg.InputText(tooltip="Enter task")
add_botton = sg.Button("Add")

window = sg.Window("My Tasks App", layout=[[label, input_box, add_botton]])
window.read()
window.close()