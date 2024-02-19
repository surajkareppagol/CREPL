from sys import exit

from compile import compile_and_run
from console import Terminal
from template import write_to_template

console = Terminal()

line = 5
template_content = ""

snapshot = ""


with open("template.c", "r") as template:
    data = template.readlines()
    template_content = "".join(data)
    snapshot_content = data[:]

console.clear()
console.print_panel("CREPL - C Read Eval Print Loop")

while True:
    try:
        user_code = console.input("[bold green]Input[/bold green]: ")
    except KeyboardInterrupt:
        with open("template.c", "w") as template:
            template.write(template_content)
        exit(1)

    if user_code in ["exit", "exit()"]:
        with open("template.c", "w") as template:
            template.write(template_content)
        console.clear()
        break
    elif user_code in ["clear"]:
        console.clear()
        console.print_panel("CREPL - C Read Eval Print Loop")
        continue

    snapshot_content = data[:]
    write_to_template(user_code, line, data)
    line = line + 2

    if not compile_and_run(snapshot_content):
        data = snapshot_content[:]
        line = line - 2
