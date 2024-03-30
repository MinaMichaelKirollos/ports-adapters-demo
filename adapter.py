"""Implements the print adapter using the print port."""

from port import PrintAdapterPort


class ConsolePrintAdapter(PrintAdapterPort):
    def print_number(self, number: int):
        print(f"The random number is: {number}")
