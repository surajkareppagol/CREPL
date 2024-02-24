import os
import re

from compile import compile_and_run
from console import Terminal
from util import clear_and_print, write_template


class CodeInput(Terminal):
    def __init__(self) -> None:
        super().__init__()

        self.code_cell = 1

        # Multi Line

        self.multi_line_global = False
        self.multi_line_local = False

        self.pop_from = ""

        self.wrote_to_template = False

        self.multi_line_code = ""

        self.completed = False

        self.brackets_valid = []

        self.scope = ""

        # Types

        self.file_global = []
        self.file_local = []
        self.file_functions = []

        self.syntax_tokens = ["if", "else", "for", "while"]

        self.function_regex = re.compile(r"[a-z]*\s[a-z]*\(.*\)+{")

    def initialise_template(self):
        self.file_global = [
            "#include <stdio.h>\n",
        ]

        self.file_functions = []

        self.file_local = [
            "int main(){\n",
        ]

    def handle_keywords(self, keyword):
        if keyword == None:
            return

        if keyword in ["exit", "exit()"]:
            if os.path.isfile("./template.c"):
                os.unlink("./template.c")
            super().clear()
            exit(0)
        elif keyword in ["clear", "clear()"]:
            clear_and_print()
            return "clear"
        elif keyword in ["reset", "reset()"]:
            return "reset"
        elif keyword in ["show", "show()"]:
            return "show"

    def check_scope(self, code):
        for token in self.syntax_tokens:
            if token in code:
                return "l"

        function_match = self.function_regex.match(code)

        if function_match:
            return "g"
        else:
            return None

    def handle(self, code):
        handler = self.handle_keywords(code)

        # 0 - Continue
        if handler == "clear":
            self.code_cell += 1
            return 0
        elif handler == "reset":
            self.code_cell += 1
            self.initialise_template()
            return 0
        elif handler == "show":
            if os.path.isfile("./template.c"):
                with open("template.c") as file:
                    super().print_panel("".join(file.readlines()))
            self.code_cell += 1
            return 0

        if self.brackets_valid and code.strip() == "}":
            self.brackets_valid.pop()

        if "}" in code and not self.brackets_valid:
            self.multi_line_code += f"{code}\n"

            if self.multi_line_local:
                self.pop_from = "l"
                self.file_local.append(self.multi_line_code)
            elif self.multi_line_global:
                self.pop_from = "g"
                self.file_functions.append(self.multi_line_code)

            self.multi_line_code = ""

            self.multi_line_local = False
            self.multi_line_global = False

            self.wrote_to_template = True

            self.completed = True

        if not self.multi_line_global and not self.multi_line_local:
            self.scope = self.check_scope(code)

        # In local scope
        if (self.multi_line_local or self.scope == "l") and not self.completed:
            self.multi_line_code += f"{code}\n"
            self.multi_line_local = True
            if "{" in code:
                self.brackets_valid.append("{")
            return 0

        # In global scope
        elif (self.multi_line_global or self.scope == "g") and not self.completed:
            self.multi_line_code += f"{code}\n"
            self.multi_line_global = True
            if "{" in code:
                self.brackets_valid.append("{")
            return 0

        if "global:" in code or "g:" in code:
            code = code.split(":")[1].strip()
            self.file_global.append(f"{code}\n")

            self.wrote_to_template = True

        if not self.wrote_to_template:
            self.pop_from = "l"
            self.file_local.append(f"{code}\n")

        self.wrote_to_template = False
        self.completed = False

        write_template(self.file_global, self.file_functions, self.file_local)

        if not compile_and_run():
            if self.pop_from == "g":
                self.file_functions.pop()
            else:
                self.file_local.pop()
        else:
            self.code_cell += 1

        return 1
