from os import unlink
from os.path import isfile
from sys import exit

from compile import compile_and_run
from console import Terminal
from input import CodeInput
from util import *

console = Terminal()
code_input = CodeInput()

code_input.initialise_template()

clear_and_print()

while True:
    try:
        if not code_input.multi_line_local and not code_input.multi_line_global:
            console.rule(
                f"Code Cell {code_input.code_cell}", style="bold yellow", align="center"
            )
            console.print("INPUT :", end="", style="bold i cyan")
            code = console.input(" ")
        else:
            code = console.input(" " * 8)
    except KeyboardInterrupt:
        if isfile("./template.c"):
            unlink("./template.c")
        console.print("[bold red]CTRL + C[/bold red] Pressed.")
        exit(0)

    if not code_input.handle(code):
        continue
