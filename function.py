FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """read files"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """store item in files #open(name_of_files, w/r/x) #writelines(list)
"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

