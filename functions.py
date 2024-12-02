FILEPATH = 'todos.txt'
def get_todos(filename=FILEPATH):
    with open(filename, 'r') as file:
        todos = file.readlines()
    return todos

def write_todos(todos, filename=FILEPATH):
    with open(filename, 'w') as file:
        file.writelines(todos)


if __name__ == '__main__':
    print('Functions file is getting executed')