Sudoku Solver
==============

Sudoku solver finishes basic 9x9 sudoku number puzzles.

Puzzle data is input using a text file pointed to inside command line.

```
~/sudoku/src$ python sudoku.py -h
usage: sudoku.py [-h] [--puzzle PUZZLE]

Sudoku Puzzle

optional arguments:
  -h, --help       show this help message and exit
  --puzzle PUZZLE  file name containing puzzle data

~/sudoku/src$ cat sudoku.txt
.31.9...5
.98......
....8..21
8.6.14..9
....5....
3..67.1.8
17..4....
......69.
4...2.51.

~/sudoku/src$ python sudoku.py --puzzle=sudoku.txt

. 3 1 | . 9 . | . . 5
. 9 8 | . . . | . . .
. . . | . 8 . | . 2 1
- - - + - - - + - - -
8 . 6 | . 1 4 | . . 9
. . . | . 5 . | . . .
3 . . | 6 7 . | 1 . 8
- - - + - - - + - - -
1 7 . | . 4 . | . . .
. . . | . . . | 6 9 .
4 . . | . 2 . | 5 1 .

7 3 1 | 4 9 2 | 8 6 5
2 9 8 | 1 6 5 | 4 7 3
6 4 5 | 3 8 7 | 9 2 1
- - - + - - - + - - -
8 5 6 | 2 1 4 | 7 3 9
9 1 7 | 8 5 3 | 2 4 6
3 2 4 | 6 7 9 | 1 5 8
- - - + - - - + - - -
1 7 9 | 5 4 6 | 3 8 2
5 8 2 | 7 3 1 | 6 9 4
4 6 3 | 9 2 8 | 5 1 7
```
