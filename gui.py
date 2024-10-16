import module
import FreeSimpleGUI as sg
import module
import time

sg.theme("black")
clock = sg.Text("",key="clock")

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to-do", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(key="todos", values=module.todo_fun(),
                      enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")
complete_button = sg.Button("complete")
exit_button = sg.Button("Exit")

window = sg.Window("My-To-Do-App",
                   layout=[[clock],[label], [input_box, add_button],
                           [list_box, edit_button,complete_button],
                            [exit_button]],
                   font=("Helvetica", 20))

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(time.strftime("%b,%m,%y,%H,%M,%S"))

    match event:
        case "Add":
            todos = module.todo_fun()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            module.write_todo(todos)
            window["todos"].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values['todo']

                todos = module.todo_fun()
                index = todos.index(todo_to_edit)

                todos[index] = new_todo
                module.write_todo(todos)
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("Please select one item first.",font=("Helevetica",20))

        case "complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = module.todo_fun()
                todos.remove(todo_to_complete)
                module.write_todo(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                sg.popup("Please select the item first",font=("Helvetica",20))
        case "Exit":
            break
        case "todos":
            window["todo"].update(value=values['todos'][0])


        case sg.WIN_CLOSED:
            break

window.close()
