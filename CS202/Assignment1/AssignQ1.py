import time
import argparse
from inp_out import *
from solver import *

parser = argparse.ArgumentParser()
parser.add_argument("-k", type=int, default=3, help="Value of k for the sudoku")
parser.add_argument("-csv", type=str, default="sudoku1.csv", help="Input Csv file name. E.g: \"suduok1.csv\"")
args = parser.parse_args()

start = time.time()
k = args.k
file = args.csv

s1, s2 = readData(inputCSV(file), k) 

# Useful for generating empty sudokus: 
# s1, s2 = [[0 for i in range(k**2)] for j in range(k**2)], [[0 for i in range(k**2)] for j in range(k**2)]

s1, s2 = solveSudokuPair(s1, s2, k)
outputData(s1, s2)

end = time.time()
print(end - start)