## Usage

### Windows
```
g++ ./main.cpp ./solver.cpp
./a.exe
```

### Linux
```
g++ .\main.cpp .\solver.cpp
.\a.out
```

## Directory Structure

```bash
Assignment2
│───README.md
│───Report.pdf
│   
│───main.cpp
│
│───solver.hpp
│───solver.hpp
│
└───tests
```

## Directory details 
The details of each file are given below:

1. [main.cpp](main.cpp) : Contains the main function, that solves the given testcases. 

2. [solver.hpp](solver.hpp) : This is a `C++ Header File` containing the declaration of **solver** class and its member functions, variables.

3. [solver.cpp](solver.cpp) : This file contains the definition of the member functions of **solver** class, declared in *solver.hpp*.

    1. `add_clause(clause)`: Adds the the given input clause (a vector of integers) to **clauses** which is a *public* variable of **solver** class containing the given formula in CNF format.\
    This function also checks if the given input clause is a `tautology`. If yes, then the clause is not inserted in the formula, as the given clause will always be true.

    2. `unit_literal()`: Checks if there is a clause in the formula with only one literal. If yes, the literal has to be satisfied for the CNF to satisfy. Hence, we insert this literal to **fixed** which is a *private* variable of the **solver** class containing the literals whose truth values are fixed.

    3. `pure_literal()`: Checks if any literal is pure in the given formula, i.e., at all occurrences of the literal in the CNF formula, it is always either *p* or *-p*. If any literal is pure, then we can again assign its truth value to *true* (or *false*), as it can never generate a contradiction. Hence, we insert this literal to **fixed**.

    4. `clean()`: Cleans the CNF formula in the following two ways:
        
        1. For every literal present in **fixed**, since its value is assigned to *true*, we remove all the clauses which contain this literal from the CNF formula as the clause is already satisfied.

        2. For every literal present in **fixed**, if any clause contains _negation_ of that literal, then that literal is erased from the clause. \
        <u>Note</u> If this step results in an empty clause, then the CNF cannot be satisfied.

    5. `clean_DPLL()`: Continuously cleans the CNF formula using above described `clean()` function unless further cleaning is not possible.

    6. `solve()`: This is the main function in the SAT Solver. It cleans the CNF formula using `clean_DPLL()` and then recursively calls itself using the standard [DPLL Algorithm](https://en.wikipedia.org/wiki/DPLL_algorithm) with some basic branching heuristics to optimise run-time.

    7. `read_cnf(file)`: Reads a CNF formula from the given input _"file"_ (`.cnf`/ `DIMACS`) and stores it as a list of lists (set of sets to be precise).

    8. `get_model()`: Whenever the CNF is satisfiable, this function returns a model solution in the form of vector of integers (in which each integer represents a literal). Its use is undefined when the CNF is unsatisfiable. 

    9. `print_model()`: Prints the model solution obtained from the above described `get_model()` function.

    10. `max_two_clause()`: Used as a branching heuristic to optimise the standard DPLL algorithm.Instead of choosing a random literal first, it returns the literal with maximum occurrences in (dynamic) clauses of size=_2 literals_.

    11. `max_three_clause()`: Used as a branching heuristic to optimise the standard DPLL algorithm, in case the above heuristic does not return a valid literal. Instead of choosing a random literal first, it returns the literal with maximum occurrences in (dynamic) clauses of size=_3 literals_.

    12. `max_occurences()`: Used as a branching heuristic to optimise the standard DPLL algorithm, in case the above heuristic does not return a valid literal. Instead of choosing a random literal first, it returns the literal with maximum occurrences in (dynamic) clauses. Trivially guarantees to return a literal if CNF is not empty<br>
    <u>Note:</u> None of the three heuristics differentiate between a literal and its negation.

4. [Documentation](Report.pdf) : Describes our approach towards making the SAT solver.

5. <u>tests/</u> Includes some small test cases in DIMACS format to test the model on. But, the model was tested on multiple SAT, UNSAT (CNF) expressions of size `150 literals, 645 clauses` too.