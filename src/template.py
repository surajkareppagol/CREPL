from util import read_write_file


def write_to_template(code, line, data):
    # Start inserting from line 5

    for i in range(1, len(data) + 1):
        if i == line:
            data.insert(line, f"{code}\n")
            data.insert(line + 1, " \n")

    read_write_file("template.c", "w", "".join(data))
