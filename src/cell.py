# cell.py
#
# A cell is a entity inside a grid referencing a row, column, and box


class CellException(BaseException):
    pass

class Cell:
    POSSIBLE_ANSWERS = set([1, 2, 3, 4, 5, 6, 7, 8, 9])

    def __init__(self, row, col, box):
        self._row = row
        self._col = col
        self._box = box
        self.num = None
        self.disallowed = set()

    def can_insert(self, num):
        return num not in self._row.union(self._col).union(self._box)

    def insert(self, num):
        if not self.can_insert(num):
            # print self._row, self._col, self._box, num
            raise CellException()
        self._row.add(num)
        self._col.add(num)
        self._box.add(num)
        self.num = num
        #print self._row, self._col, self._box, num

    def erase(self):
        self._row.remove(self.num)
        self._col.remove(self.num)
        self._box.remove(self.num)
        self.num = None

    def disallow(self):
        if self.num is not None:
            self.disallowed.add(self.num)
            self.erase()
