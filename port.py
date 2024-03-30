"""Interface between the print adapter for the app to print a random number"""

from abc import ABC, abstractmethod


class PrintAdapterPort(ABC):
    @abstractmethod
    def print_number(self, number: int):
        return
