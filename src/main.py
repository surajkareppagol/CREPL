from sys import exit

from compile import compile_and_run
from console import Terminal
from util import *

console = Terminal()

code_cell = 1

# Multi Line

multi_line_global = False
multi_line_local = False

pop_from = ""

wrote_to_template = False

multi_line_code = ""

completed = False

brackets_valid = []

# Types

file_global, file_local, file_functions = [], [], []


def initialise_template():
    global file_global
    file_global = [
        "#include <stdio.h>\n",
    ]

    global file_functions
    file_functions = []

    global file_local
    file_local = [
        "int main(){\n",
    ]


initialise_template()

clear_and_print()

while True:
    try:
        if not multi_line_local and not multi_line_global:
            console.rule(f"Code Cell {code_cell}", style="bold yellow", align="center")
            console.print("INPUT :", end="", style="bold i cyan")
            code = console.input(" ")
        else:
            code = console.input(" " * 8)
    except KeyboardInterrupt:
        os.unlink("./template.c")
        console.print("[bold red]CTRL + C[/bold red] Pressed.")
        exit(0)

    handler = handle_keywords(code)

    if handler == "clear":
        code_cell += 1
        continue
    elif handler == "reset":
        code_cell += 1
        initialise_template()
        continue
    elif handler == "show":
        with open("template.c") as file:
            console.print_panel("".join(file.readlines()))
        code_cell += 1
        continue

    if brackets_valid and code.strip() == "}":
        brackets_valid.pop()

    if "}" in code and not brackets_valid:
        multi_line_code += f"{code}\n"

        if multi_line_local:
            pop_from = "l"
            file_local.append(multi_line_code)
        elif multi_line_global:
            pop_from = "g"
            file_functions.append(multi_line_code)

        multi_line_code = ""

        multi_line_local = False
        multi_line_global = False

        wrote_to_template = True

        completed = True

    if not multi_line_global and not multi_line_local:
        scope = check_scope(code)

    # In local scope
    if (multi_line_local or scope == "l") and not completed:
        multi_line_code += f"{code}\n"
        multi_line_local = True
        if "{" in code:
            brackets_valid.append("{")
        continue

    # In global scope
    elif (multi_line_global or scope == "g") and not completed:
        multi_line_code += f"{code}\n"
        multi_line_global = True
        if "{" in code:
            brackets_valid.append("{")
        continue

    if "global:" in code or "g:" in code:
        code = code.split(":")[1].strip()
        file_global.append(f"{code}\n")

        wrote_to_template = True

    if not wrote_to_template:
        pop_from = "l"
        file_local.append(f"{code}\n")

    wrote_to_template = False
    completed = False

    write_template(file_global, file_functions, file_local)

    if not compile_and_run():
        if pop_from == "g":
            file_functions.pop()
        else:
            file_local.pop()
    else:
        code_cell += 1
