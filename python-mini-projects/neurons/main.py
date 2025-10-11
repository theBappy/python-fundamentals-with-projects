import os
import random
import sys
import time
from enum import Enum
from shutil import get_terminal_size

FPS = 10


def clear() -> None:
    """Clear the terminal based on OS."""
    os.system("cls" if sys.platform == "win32" else "clear")


class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class Empty(str):
    CHAR = "  "

    def __new__(cls) -> str:
        return str.__new__(cls, cls.CHAR)


class Neuron(str):
    CHAR = "██"
    CHANCE_OF_DEATH = 35  # percent chance neuron dies per frame

    def __new__(cls) -> str:
        return str.__new__(cls, cls.CHAR)


class Grid:
    """Class to store and update the grid."""

    def __init__(self, width, height) -> None:
        # Ensure minimum grid size
        width = max(5, width)
        height = max(5, height)
        self.width = width
        self.height = height
        self._grid = [[Empty() for _ in range(width)] for _ in range(height)]

    def __str__(self) -> str:
        return "\n".join("".join(row) for row in self._grid)

    @property
    def neurons(self):
        """Return list of neurons and their coordinates."""
        return [
            (x, y)
            for y, row in enumerate(self._grid)
            for x, element in enumerate(row)
            if isinstance(element, Neuron)
        ]

    def set_neuron(self, x, y) -> None:
        if 0 <= x < self.width and 0 <= y < self.height:
            self._grid[y][x] = Neuron()

    def tick(self) -> None:
        """Randomly kill or move all Neurons safely."""
        neurons = list(self.neurons)  # snapshot

        for x, y in neurons:
            # Check if the neuron still exists (might be replaced already)
            if not isinstance(self._grid[y][x], Neuron):
                continue

            # Possibly kill neuron
            if random.randint(1, 100) <= Neuron.CHANCE_OF_DEATH:
                self._grid[y][x] = Empty()
                continue

            # Calculate new position
            direction = random.choice(list(Direction))
            new_x, new_y = x, y

            if direction == Direction.UP:
                new_y -= 1
            elif direction == Direction.RIGHT:
                new_x += 1
            elif direction == Direction.DOWN:
                new_y += 1
            elif direction == Direction.LEFT:
                new_x -= 1

            # ✅ Check boundaries before moving
            if 0 <= new_x < self.width and 0 <= new_y < self.height:
                self._grid[y][x] = Empty()
                self._grid[new_y][new_x] = Neuron()
            # If out of bounds — stay in place
            else:
                continue



def main() -> None:
    """Run the program."""
    term_width, term_height = get_terminal_size()
    grid_width = term_width // len(Neuron.CHAR)
    grid_height = max(5, term_height - 1)  # prevent bottom overflow

    grid = Grid(grid_width, grid_height)

    # Add some starting neurons
    grid.set_neuron(15, 10)
    grid.set_neuron(35, 15)

    while grid.neurons:
        clear()
        print(grid)
        grid.tick()
        time.sleep(1 / FPS)


if __name__ == "__main__":
    main()
