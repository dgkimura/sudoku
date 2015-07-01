# grid.py
#
# A grid is an entity that consists of 81 cells. Each cell is a unique
# combination of row, col, and box.
from cell import Cell


class Grid:
    GRID_ROWS = [set(), set(), set(), set(), set(), set(), set(), set(), set()]
    GRID_COLS = [set(), set(), set(), set(), set(), set(), set(), set(), set()]
    GRID_BOXS = [set(), set(), set(), set(), set(), set(), set(), set(), set()]

    def __init__(self):
        self.cells = []
        for n in range(81):
            r = self.GRID_ROWS[n / 9]
            c = self.GRID_COLS[n % 9]
            b = self.GRID_BOXS[((n / 3) % 3) + ((n / 27) * 3)]
            self.cells.append(Cell(r, c, b))

    def __str__(self):
        grid = ""
        for n in range(81):
            line = ""
            if n % 3 == 0:
                line = "| "
            if n % 9 == 0:
                line = "\n"
            if n % 27 == 0 and n is not 0:
                line = "\n- - - + - - - + - - -\n"
            grid += line + ("{0} ".format(self.cells[n].num or "."))
        return grid
