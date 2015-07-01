"""Sudoku module

"""
from argparse import ArgumentParser

from grid import Grid
from solver import Solver

# A A A | B B B | C C C
# A A A | B B B | C C C
# A A A | B B B | C C C
# - - - + - - - + - - - 
# D D D | E E E + F F F
# D D D | E E E + F F F
# D D D | E E E + F F F
# - - - + - - - + - - - 
# G G G | H H H | I I I
# G G G | H H H | I I I
# G G G | H H H | I I I

#raw_puzzle = """
#.86..3...
#..4.78...
#.3.24....
#3...2..4.
#7.......2
#.4..8...1
#....32.9.
#...79.3..
#...8..51.
#"""

def parse_args():
    parser = ArgumentParser(description='Sudoku Puzzle')
    parser.add_argument('--puzzle', type=str, default='sudoku.txt',
        help="file name containing puzzle data")
    args = parser.parse_args()
    return args


def puzzle_start_input(raw_puzzle):
    tmp_puzzle = ''.join([i.strip() for i in raw_puzzle])
    return [int(n) if n is not "." else None for n in list(tmp_puzzle)]


def main():
    args = parse_args()
    f = open(args.puzzle)

    g = Grid()
    s = Solver(g)
    s.populate(puzzle_start_input(f.readlines()))
    print g
    s.solve()
    print g

if __name__ == '__main__':
    main()
