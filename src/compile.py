import os
import subprocess

from console import Terminal

console = Terminal()


def compile_and_run(snapshot_content):
    compiler_out = subprocess.run(
        ["gcc", "template.c", "-o", "template"], capture_output=True
    )

    if not os.path.isfile("./template"):
        output = str(compiler_out.stderr, encoding="utf-8")
        console.print_panel(output)

        with open("template.c", "w") as template:
            template.write("".join(snapshot_content))

        return 0

    execution_out = subprocess.run(["./template"], capture_output=True)

    output = str(execution_out.stdout, encoding="utf-8").strip()

    console.print("[bold red]Output[/bold red]:")

    print(output, "\n")

    if os.path.isfile("./template"):
        os.unlink("./template")

    return 1
