import re

from compile import compile_and_run
from console import Terminal
from util import *


class CodeInput(Terminal):
    def __init__(self) -> None:
        super().__init__()

        self.code_cell = 1

        # Multi Line

        self.multi_line_global = False
        self.multi_line_local = False
        self.wrote_to_template = False
        self.input_completed = False
        self.pop_from = True

        # True = Global, False = Local

        self.multi_line_code = ""

        self.brackets_valid = []

        # Formatting

        self.scope = ""
        self.space = 2

        # Types

        self.file_global = []
        self.file_local = []
        self.file_functions = []

        self.syntax_tokens = ["if", "else", "for", "while"]

        self.function_regex = re.compile(r"[a-z]*\s[^0-9][a-z_A-Z]*\(.*\)+{")

    def initialise_template(self):
        self.file_global = [
            "#include <stdio.h>\n",
        ]

        self.file_functions = []

        self.file_local = [
            "int main(){\n",
        ]

    def check_scope(self, code):
        for token in self.syntax_tokens:
            if token in code:
                self.multi_line_local = True
                return

        function_match = self.function_regex.match(code)

        if function_match:
            self.multi_line_global = True
            return
        else:
            return None

    def handle_keywords(self, keyword):
        if keyword in ["exit", "exit()"]:
            delete_template("template.c")
            super().clear()
            exit(0)

        elif keyword in ["clear", "clear()"]:
            self.code_cell += 1
            clear_and_print()
            return 0

        elif keyword in ["reset", "reset()"]:
            self.code_cell += 1
            self.initialise_template()
            return 0

        elif keyword in ["show", "show()"]:
            code = read_template("template.c")
            super().print_panel(code)

            self.code_cell += 1
            return 0

        return 1

    def handle_input(self, code):
        handler = self.handle_keywords(code)

        if not handler:
            return 0

        if self.brackets_valid and code.strip() == "}":
            self.space = (len(self.brackets_valid) - 1) * 2
            self.brackets_valid.pop()

        if "}" in code and not self.brackets_valid:
            self.multi_line_code += f"{code}\n\n"

            if self.multi_line_local:
                self.pop_from = False
                self.file_local.append(f"\n{self.multi_line_code}")
            elif self.multi_line_global:
                self.pop_from = True
                self.file_functions.append(f"\n{self.multi_line_code}")

            self.multi_line_code = ""

            self.multi_line_local = False
            self.multi_line_global = False

            self.wrote_to_template = True
            self.input_completed = True

        if not self.multi_line_global and not self.multi_line_local:
            self.scope = self.check_scope(code)

        if (
            self.multi_line_local or self.multi_line_global
        ) and not self.input_completed:
            self.space = len(self.brackets_valid) * 2

            self.multi_line_code += f"{self.space * ' '}{code}\n"
            if "{" in code:
                self.brackets_valid.append("{")
            return 0

        if "global:" in code or "g:" in code:
            code = code.split(":")[1].strip()
            self.file_global.append(f"{code}\n")

            self.wrote_to_template = True

        # Local scope for single line code
        if not self.wrote_to_template:
            self.pop_from = False
            self.file_local.append(f"{2 * ' '}{code}\n")

        self.wrote_to_template = False
        self.input_completed = False

        write_template(self.file_global, self.file_functions, self.file_local)

        if not compile_and_run():
            if self.pop_from:
                self.file_functions.pop()
            else:
                self.file_local.pop()
        else:
            self.code_cell += 1

        return 1
