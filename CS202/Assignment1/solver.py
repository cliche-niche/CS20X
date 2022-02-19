from clauses import *
from utils import *
from inp_out import *
from pysat.solvers import Solver

def solveSudokuPair(s1, s2, k):
    # Pair Sudoku Solver for given sudokus, s1 and s2. Fills them and returns them
    sol = Solver()

    clauses = []
    assumption = []

    for i in range(k**2):
        for j in range(k**2):
            add_cell(assumption, i, j, 0, s1[i][j], k) # Adding assumptions in case the cell is already filled
            add_cell(assumption, i, j, 1, s2[i][j], k)
            clause = cell_diff(i, j, s1[i][j], s2[i][j], k)
            clauses = clauses + clause

    clauses = clauses + add_rows(0, k) + add_cols(0, k) + add_box(0, k) + cell_clause(0, k) # Adding all the clauses
    clauses = clauses + add_rows(1, k) + add_cols(1, k) + add_box(1, k) + cell_clause(1, k)

    for c in clauses:
        sol.add_clause(c)

    sol.solve(assumptions = assumption)

    s3 = None

    for s in sol.enum_models(assumptions = assumption):
        s3 = make_sudoku_pair(s, k)
        break

    if s3 == None :
        return None, None

    s1 = []
    s2 = []
    for i in range(k**2):
        row = []
        for j in range(k**2):
            row.append(s3[i*k**2+j])
        s1.append(row)
    
    for i in range(k**2):
        row = []
        for j in range(k**2):
            row.append(s3[k**4+i*k**2+j])
        s2.append(row)

    sol.delete()

    return s1, s2

def solveSudoku(s1, k):
    # Single Sudoku solver. Solves s1 of size k*k
    tempSolver = Solver()

    assumption = []
    for i in range(k**2):
        for j in range(k**2):
            add_cell(assumption, i, j, 0, s1[i][j], k)

    clauses = []
    clauses = clauses + add_cols(0, k) + add_rows(0, k) + add_box(0, k) + cell_clause(0, k)

    for i in clauses:
        tempSolver.add_clause(i)
    
    tempSolver.solve(assumptions = assumption)

    model = tempSolver.get_model()
    s1 = make_sudoku(model, k)

    s = []
    for i in range(k**2):
        temp = []
        for j in range(k**2):
            temp.append(s1[i*k**2+j])
        s.append(temp)

    tempSolver.delete()

    return s

def generate_filled(k):
    # Generates two filled sudokus of size k
    sud1 = []
    sud2 = []

    # Initializing the sudoku to be empty (0 everywhere)
    for i in range(k**2):
        row = []
        for j in range(k**2):
            row.append(0)
        sud1.append(row)

    # Randomly filling the sudoku
    sud1 = randomise_sudoku(sud1, k)
    sud1 = solveSudoku(sud1, k)

    # Making sud2 empty (0 everywhere)
    sud2 = []
    for i in range(k**2):
        row = []
        for j in range(k**2):
            row.append(0)
        sud2.append(row)
    
    # Solver generates a pair
    sud1, sud2 = solveSudokuPair(sud1, sud2, k)

    return sud1, sud2

def num_solutions(s1, s2, k):
    # Determines if the pair has a unique solution or more than one solutions; Returns 1 or 2
    sol = Solver()

    clauses = []
    assumption = []

    for i in range(k**2):
        for j in range(k**2):
            add_cell(assumption, i, j, 0, s1[i][j], k)
            add_cell(assumption, i, j, 1, s2[i][j], k)
            clause = cell_diff(i, j, s1[i][j], s2[i][j], k)
            clauses = clauses + clause


    clauses = clauses + add_rows(0, k) + add_cols(0, k) + add_box(0, k) + cell_clause(0, k)
    clauses = clauses + add_rows(1, k) + add_cols(1, k) + add_box(1, k) + cell_clause(1, k)

    for i in clauses:
        sol.add_clause(i)

    sol.solve(assumptions = assumption)


    answers = set() # Storing the sudokus in a set just to be robust
    for i in sol.enum_models(assumptions = assumption):
        s3 = make_sudoku_pair(i, k)
        answers.add(tuple(s3))
        if(len(answers) > 1):
            break

    return len(answers)

def generator(s1, s2, k):
    # Deletes entries from a filled pair until maximality

    cells = [z for z in range(2*k**4)]
    
    for _ in range(k**2):
        random.shuffle(cells) # So that the order of cells is not the same each time the function is called

    for c in cells:
        
        s = c//(k**4)
        i = (c-s*k**4)//(k**2)
        j = c%(k**2)

        if s==1:
            t = s2[i][j]
            s2[i][j] = 0
        else:
            t = s1[i][j]
            s1[i][j] = 0
        
        if (num_solutions(s1, s2, k)>1):
            if s==1:
                s2[i][j] = t
            else:
                s1[i][j] = t
    
    return s1, s2
    