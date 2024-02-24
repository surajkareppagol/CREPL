from os import unlink
from os.path import isfile

from console import Terminal

console = Terminal()


def write_template(file_global, file_functions, file_local):
    with open("template.c", "w") as file:
        file.write("".join(file_global))
        file.write("".join(file_functions))
        file.write("".join(file_local))

        file.write("  return 0;\n}")


def delete_template(file):
    if isfile(file):
        unlink(file)


def read_template(file):
    if isfile(file):
        with open(file) as file:
            data = file.readlines()
            code = ""
            for i, line in enumerate(data, start=1):
                code += f"[bold green]{i}[/bold green]{' ' * len(str(len(data)))}{line}"

    return code


def clear_and_print():
    console.clear()
    console.print_panel("[bold green]CREPL[/bold green] - C Read Eval Print Loop")
