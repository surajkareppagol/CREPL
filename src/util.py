import os
import re

from console import Terminal

console = Terminal()

syntax_tokens = ["if", "else", "for", "while"]

function_regex = re.compile(r"[a-z]*\s[a-z]*\(.*\)+{")


def write_template(file_global, file_functions, file_local):
    with open("template.c", "w") as file:
        file.write("".join(file_global))
        file.write("".join(file_functions))
        file.write("".join(file_local))

        file.write("return 0;\n}")


def clear_and_print():
    console.clear()
    console.print_panel("[bold green]CREPL[/bold green] - C Read Eval Print Loop")


def handle_keywords(keyword):
    if keyword == None:
        return

    if keyword in ["exit", "exit()"]:
        if os.path.isfile("./template.c"):
            os.unlink("./template.c")
        console.clear()
        exit(0)
    elif keyword in ["clear", "clear()"]:
        clear_and_print()
        return "clear"
    elif keyword in ["reset", "reset()"]:
        return "reset"
    elif keyword in ["show", "show()"]:
        return "show"


def check_scope(code):
    for token in syntax_tokens:
        if token in code:
            return "l"

    function_match = function_regex.match(code)

    if function_match:
        return "g"
    else:
        return None
