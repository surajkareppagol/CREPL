from console import Terminal

console = Terminal()


def write_template(file_global, file_functions, file_local):
    with open("template.c", "w") as file:
        file.write("".join(file_global))
        file.write("".join(file_functions))
        file.write("".join(file_local))

        file.write("return 0;\n}")


def clear_and_print():
    console.clear()
    console.print_panel("[bold green]CREPL[/bold green] - C Read Eval Print Loop")
