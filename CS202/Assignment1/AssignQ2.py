import time
import argparse
import csv

from solver import *

parser = argparse.ArgumentParser()
parser.add_argument("-k", type=int, default=3)
parser.add_argument("-o", "--output", type=int, default=1, help="Number of .csv files to output")
args = parser.parse_args()
start = time.time()

k = args.k
outputs = args.output

for i in range(outputs):
    # Generates and writes sudoku pairs to .csv files in the same directory
    s1, s2 = generate_filled(k)
    s1, s2 = generator(s1, s2, k)
    
    combined = s1 + s2
    name = "sudoku" + str(i + 1) + ".csv"
    with open(name, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(combined)

end = time.time()
print(end - start)