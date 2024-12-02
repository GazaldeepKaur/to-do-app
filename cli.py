from functions import *


while True:
    user_action = input('Type, add, show, edit, complete or exit:')
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]
        todos = get_todos()
        todos.append(todo + '\n')

        write_todos(todos)
        print(f'The todo {todo} has been added to the to do list')

    elif user_action.startswith('show'):
        todos = get_todos()

        for index, todo in enumerate(todos):
            print(f'{index+1} - {todo.strip('\n')}')

    elif user_action.startswith('edit'):
        edited_number = user_action[5:]
        edited_todo = input('Enter the edited todo:')

        todos = get_todos()

        todos[int(user_action[5:]) - 1] = edited_todo + '\n'
        write_todos(todos)

    elif user_action.startswith('complete'):
        try:
            complete_number = int(user_action[9:])
            if complete_number <= 0:
                raise IndexError
            todos = get_todos()

            todos.pop(complete_number-1)
            write_todos(todos)
            print(f'The todo at number {complete_number} has been completed')
        except IndexError:
            print('Entered number is not present in the todo list')
            continue

        except ValueError:
            print('Invalid Value. Enter a number')
            continue


    elif user_action.startswith('exit'):
        break






