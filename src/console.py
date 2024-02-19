from rich.console import Console
from rich.panel import Panel


class Terminal(Console):
    def __init__(self):
        super().__init__()

    def print_panel(self, string: str) -> None:
        super().print(Panel(string))
