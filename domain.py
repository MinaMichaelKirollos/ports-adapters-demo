"""Basic logic for ports and adapters ddemo of generating a random number between 1 and 10."""

import random


class RandomNumberGenerator:
    def generate(self):
        return random.randint(1, 10)
