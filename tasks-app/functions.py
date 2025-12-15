FILEPATH = "tasks.txt"

def get_tasks(filepath=FILEPATH):
    """Returns the content of the specified file"""
    with open(filepath, "r") as doc:
        content = doc.readlines()
    return content


def write_tasks(content, filepath=FILEPATH):
    """Writes content to a text file"""
    with open(filepath, "w") as doc:
        doc.writelines(content)
