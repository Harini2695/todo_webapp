FILEPATH = "todos.txt"
def get_todos(filepath=FILEPATH): # as filepath is a default argument we are defining it here
    """Read a text file
    and return the list of to-do items
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg,filepath = FILEPATH):  # parameters:filepath and what we need to write
    """
    Write and update the to-do list in the file
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


