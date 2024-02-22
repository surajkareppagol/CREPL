import os
import subprocess

from console import Terminal

console = Terminal()


def compile_and_run():
    compiler_out = subprocess.run(
        ["gcc", "template.c", "-o", "template"], capture_output=True
    )

    # Check if file compiled correctly

    if not os.path.isfile("./template"):
        output = str(compiler_out.stderr, encoding="utf-8")
        console.print_panel(output)
        os.unlink("./template.c")
        return 0

    execution_out = subprocess.run(["./template"], capture_output=True)

    output = str(execution_out.stdout, encoding="utf-8").strip()

    console.print("\nOUTPUT:", style="bold i yellow")

    console.print(output, "\n")

    if os.path.isfile("./template"):
        os.unlink("./template")

    return 1
