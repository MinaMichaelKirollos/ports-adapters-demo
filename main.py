"Runner for project."

from adapter import ConsolePrintAdapter
from domain import RandomNumberGenerator

generator = RandomNumberGenerator()
adapter = ConsolePrintAdapter()

number = generator.generate()
adapter.print_number(number)
