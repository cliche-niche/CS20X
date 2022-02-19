import csv

def inputCSV(file):
    # Reads data from a file and stores it in data
    datafile = open(file, 'r')
    datareader = csv.reader(datafile, delimiter=',')
    data = []
    for row in datareader:
        data.append(row)
        
    return data

def readData(data, k):
    # Converts data read from a file to 2 2-D lists, i.e., sudokus S1 and S2, and returns them
    s1 = []
    s2 = []
    for i in range(k**2):
        row = []
        for j in range(k**2):
            row.append(int(data[i][j]))
        s1.append(row)
    
    for i in range(k**2):
        row = []
        for j in range(k**2):
            row.append(int(data[i + (k**2)][j]))
        s2.append(row)
    
    return s1, s2

def outputData(s1, s2):
    # Prints the sudokus if they are not None on the terminal, and also makes a corresponding .csv
    if(s1 == None or s2 == None):
        combined = [[]]
    else:
        combined = s1 + s2
    
    name = "solvedSudoku.csv"

    with open(name, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(combined)

    if(s1 == None or s2 == None):
        print(None)
    else:
        print("Sudoku 1:\n")
        for i in range(len(s1)):
            for j in range(len(s1)):
                print(s1[i][j], end="   ")
            print('\n')
        print('\n\n\n')
        print("Sudoku 2:\n")
        for i in range(len(s2)):
            for j in range(len(s2)):
                print(s2[i][j], end="   ")
            print('\n')
        print('\n\n')

def inv_sudo(sudoku, k):
    for i in range(k**2):
        for j in range(k**2):
            print(sudoku[i][j], end="  ")
        print("\n")
    print("\n")