from module import todo_fun, write_todo

write = """
This is the first line
this is the second line
this is third line 
this is the fourth line
this is fifth line
"""
print(write)
while True:
    user_action = input("Enter add,show,edit,complete and exit: ")
    user_action = user_action.strip()
    if user_action.startswith("add"):
        todo = user_action[4:]
        todo = todo.title()
        todos = todo_fun()
        todos.append(todo + "\n")

        write_todo(todos)

        # new_todos = [item.strip("\n") for item in todos]
    elif user_action.startswith("show"):

        todos = todo_fun()
        for index, item in enumerate(todos, start=1):
            item = item.strip('\n')
            print(f"{index}-{item}")
    elif user_action.startswith("edit"):
        try:
            user_num = int(user_action[4:])
            user_num = user_num - 1
            todos = todo_fun()

            new_item = input("Enter new Item: ")
            todos[user_num] = new_item

            write_todo(todos)
            print(new_item)

        except ValueError:
            print("This is invalid comment. Try again!")
            continue
    elif user_action.startswith("complete"):
        try:
            item_remove = user_action[8:]
            item_remove = int(item_remove) - 1
            todos = todo_fun()
            item_removed = todos.pop(item_remove)
            print(f"{item_removed} is deleted from the list")

            write_todo(todos)
        except IndexError:
            print("You value is out of range. Check your number and try again")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("This is invalid command. Try again!")

print("Bye")
#################################################
# function without parameter
#################################################
# def todo_fun():
#     with open('files/todos.txt', 'r') as todo_local:
#         todo_list_local = todo_local.readlines()
#         return todo_list_local
#
#
# while True:
#     user_action = input("Enter add,show,edit,complete and exit: ")
#     user_action = user_action.strip()
#     if user_action.startswith("add"):
#         todo = user_action[4:]
#         todo = todo.title()
#         todos = todo_fun()
#         todos.append(todo + "\n")
#         with open("files/todos.txt", 'w') as file:
#             file.writelines(todos)
#
#             # new_todos = [item.strip("\n") for item in todos]
#     elif user_action.startswith("show"):
#
#         todos = todo_fun()
#         for index, item in enumerate(todos, start=1):
#             item = item.strip('\n')
#             print(f"{index}-{item}")
#     elif user_action.startswith("edit"):
#         try:
#             user_num = int(user_action[4:])
#             user_num = user_num - 1
#             todos = todo_fun()
#
#             new_item = input("Enter new Item: ")
#             todos[user_num] = new_item
#             with open("files/todos.txt", "w") as file:
#                 file.writelines(todos)
#             print(new_item)
#         except ValueError:
#             print("This is invalid comment. Try again!")
#             continue
#     elif user_action.startswith("complete"):
#         try:
#             item_remove = user_action[8:]
#             item_remove = int(item_remove) - 1
#             todos = todo_fun()
#             item_removed = todos.pop(item_remove)
#             print(f"{item_removed} is deleted from the list")
#
#             with open("files/todos.txt", "w") as file:
#                 file.writelines(todos)
#         except IndexError:
#             print("You value is out of range. Check your number and try again")
#             continue
#     elif user_action.startswith("exit"):
#         break
#     else:
#         print("This is invalid command. Try again!")
#
# print("Bye")
# while True:
#     user_action = input("Enter add,show,edit,complete and exit: ")
#     user_action = user_action.strip()
#     if user_action.startswith("add"):
#         todo = user_action[4:]
#         todo = todo.title()
#         with open('files/todos.txt', 'r') as file:
#             todos = file.readlines()
#         todos.append(todo+"\n")
#         with open("files/todos.txt", 'w') as file:
#             file.writelines(todos)
#
#             #new_todos = [item.strip("\n") for item in todos]
#     elif user_action.startswith("show"):
#
#         with open('files/todos.txt', 'r') as todo_list:
#             todo_list = todo_list.readlines()
#         for index, item in enumerate(todo_list, start=1):
#             item = item.strip('\n')
#             print(f"{index}-{item}")
#     elif user_action.startswith("edit"):
#         try:
#             user_num = int(user_action[4:])
#             user_num = user_num-1
#             with open("files/todos.txt","r") as file:
#                 todo_list = file.readlines()
#
#             new_item = input("Enter new Item: ")
#             todo_list[user_num] = new_item
#             with open("files/todos.txt","w") as file:
#                 file.writelines(todo_list)
#             print(new_item)
#         except ValueError:
#             print("This is invalid comment. Try again!")
#             continue
#     elif user_action.startswith("complete"):
#         try:
#             item_remove = user_action[8:]
#             item_remove = int(item_remove)-1
#             with open("files/todos.txt","r") as file:
#                 todo_list = file.readlines()
#             item_removed = todo_list.pop(item_remove)
#             print(f"{item_removed} is deleted from the list")
#
#             with open("files/todos.txt","w") as file:
#                 file.writelines(todo_list)
#         except IndexError:
#             print("You value is out of range. Check your number and try again")
#             continue
#     elif user_action.startswith("exit"):
#         break
#     else:
#         print("This is invalid command. Try again!")
#
# print("Bye")
