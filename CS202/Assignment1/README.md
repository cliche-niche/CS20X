## Usage

```
pip install python-pysat
python3 AssignQ1.py -k="x" -csv="path"
python3 AssignQ2.py -k="x"
```
_x:_ should be a positive integer (without quotes)\
_path:_ should be the path to the input `.csv` file.

## Modules used
Please make sure all these modules are available
+ `time`
+ `argparse`
+ `csv`
+ `pysat`
+ `random`

## Directory Structure

```bash
Assignment1
│───README.md
│───Analysis.pdf
│   
│───AssignQ1.py
│───AssignQ2.py
│
│───solver.py
│───utils.py
│───inp_out.py
└───clauses.py
```

## Directory details 
The details of each file are given below for the sake of completeness:
1. **AssignQ1.py** : Contains the solution for Question 1 of the assignment. Takes _k_ (dimension of sudoku) and _input csv file_ (Containing a partly filled sudoku pair) as parameters and prints the solved sudokus on the terminal and writes them into a `.csv` file as well.

2. **AssignQ2.py** : Contains the solution for Question 2 of the assignment. Takes _k_ (dimension of sudoku), _outputs_ (number of sudoku pairs to be generated) as parameters, and generates _outputs_ number of csv files each containing a valid sudoku pair.

3.  **Tests** : A subdirectory containing 5 sample test cases of size _3*3_. These were generated from **AssignQ2.py** and were solved using **AssignQ1.py**.

4. **utils.py** : Contains various custom functions described below

    1. make_sudoku_pair(r, k): Returns two filled sudokus in the form of a combined 1-D list from the model solution.

    2. make_sudoku(r, k): Returns a single sudoku in the form of a 1-D list from the model solution.

    3. randomise_sudoku(s1, k): Randomly fills a row or column or a box in an empty sudoku _s1_, with a random permutation of numbers {1, 2, 3 ... k<sup>2</sup> }. \
    This is done to provide a seed to the sudoku so that everytime a new sudoku is generated from SAT solver.

5. **inp_out.py** : Contains functions used for input and output of the program

    1. inputCSV(file): Reads the input csv file and returns a 2-D array containing both the sudokus combined.
    
    2. readData(data): Returns two sudokus from a combined 2-D array.

    3. outputData(s1, s2): Writes the given input sudokus into a single `.csv` file as an output as well as prints it on the terminal.

    4. inv_sudo(s1, k): Prints the input sudoku in the terminal.

6. **solver.py** : Contains the functions described below
    
    1. solveSudokuPair(s1, s2, k): Solves the input sudoku pair using the SAT solver, and returns the two solved sudokus.

    2. solveSudoku(s1, k): Solves the input sudoku (single) using the SAT solver, and returns the solved sudoku.

    3. generate_filled(k): Returns a solved sudoku pair (where every cell has a different value in the two sudokus) of the input dimension k.

    4. num_solutions(s1, s2, k): Returns 1 if there is a unique solution to the sudoku pair s1, s2. 
    Returns 2 otherwise.

    5. generator(s1, s2, k): Deletes entries from a filled sudoku pair until maximality is achieved.
    
7. **clauses.py** : Contains functions that return list of assumptions for the SAT solver, and list of clauses for different encodings.

    1. add_cell(*args): Adds assumptions for filled cells.

    2. add_rows(*args): Returns the list of clauses for each column to have exactly one occurence of each number in the range [1, k<sup>2</sup>].
        
    3. add_cols(*args): Returns the list of clauses for each column to have exactly one occurence of each number in the range [1, k<sup>2</sup>].
    
    4. add_box(*args): Returns the list of clauses for each box to have exactly one occurence of each number in the range [1, k<sup>2</sup>].

    5. cell_clause(*args): Returns the list of clauses for each cell to have exactly one number from the range [.1, k<sup>2</sup>].

