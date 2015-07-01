# solver.py
#
# A solver will insert numbers into a grid to solve the puzzle.


class Solver:
    def __init__(self, grid):
        self._grid = grid

    def populate(self, nums):
        for i, n in enumerate(nums):
            if n is not None:
                # print i
                self._grid.cells[i].insert(n)

    def solve(self):
        # a = SingleEntry()
        # a.run(self._grid)
        b = BruteForce()
        b.run(self._grid)
        #print self._grid


class SingleEntry:
    """
    Single entry algorithm passes over all cells and marks any cell
    that has a single valid answer.

    """
    def run(self, grid):
        updated = True

        while updated:
            updated = False
            for i, c in enumerate(grid.cells):
                if c.num is not None:
                    continue

                valid =  c.POSSIBLE_ANSWERS - c._row.union(c._col) \
                          .union(c._box)
                if (len(valid) == 1):
                    c.num = valid.pop()
                    print "SINGLE ENTRY {0} {1}".format(c.num, i)
                    updated = True

class BruteForce:
    """
    Brute force algorithm that tries every possibility and returns the
    first found answer.

    """
    def run(self, grid):
        stack = []
        while (not self.is_solved(grid.cells)):
            for i, c in enumerate(grid.cells):
                if c.num is not None:
                    continue

                if self.increment(c):
                    stack.append(c)
                else:
                    while len(stack) > 1:
                        c = stack.pop()
                        if self.increment(c):
                            stack.append(c)
                            break
                        else:
                            c.erase()
                    if len(stack) == 1:
                        c = stack.pop()
                        c.disallow()
                    break

    def is_solved(self, cells):
        for c in cells:
            if c.num is None:
                return False
        return True

    def increment(self, cell):
        start = (cell.num or 0) + 1
        for n in range(start, len(cell.POSSIBLE_ANSWERS) + 1):
            if n not in cell.disallowed and cell.can_insert(n):
                if cell.num:
                    cell.erase()
                cell.insert(n)
                # print "INCREMENT END {0}".format(self.num)
                return True
        return False
