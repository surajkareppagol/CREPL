from sys import exit

from compile import compile_and_run
from console import Terminal
from template import write_to_template
from util import read_write_file

console = Terminal()

line = 5

data = read_write_file("template.c", "r")
template_code = "".join(data)
snapshot_code = data[:]


def clear_and_print():
    console.clear()
    console.print_panel("CREPL - C Read Eval Print Loop")


clear_and_print()

while True:
    try:
        user_code = console.input("[bold green]Input[/bold green]: ").strip()

        if user_code in ["exit", "exit()"]:
            read_write_file("template.c", "w", template_code)
            console.clear()
            exit(0)
        elif user_code in ["clear", "clear()"]:
            clear_and_print()
            continue
        elif user_code in ["reset", "reset()"]:
            read_write_file("template.c", "w", template_code)
            continue
    except KeyboardInterrupt:
        read_write_file("template.c", "w", template_code)
        exit(1)

    snapshot_code = data[:]
    write_to_template(user_code, line, data)
    line = line + 2

    # If compilation fails revert to previous code

    if not compile_and_run(snapshot_code):
        data = snapshot_code[:]
        line = line - 2
