import module
import FreeSimpleGUI as sg
import module

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to-do", key="todo")
add_button = sg.Button("Add")
window = sg.Window("My-To-Do-App",
                   layout=[[label], [input_box, add_button]],
                   font=("Helevatica", 20))

while True:
    event, value = window.read()
    print(event)
    print(value)
    match event:
        case "Add":
            todos = module.todo_fun()
            new_todo = value["todo"] + "\n"
            todos.append(new_todo)
            module.write_todo(todos)
        case sg.WIN_CLOSED:
            break

window.close()
