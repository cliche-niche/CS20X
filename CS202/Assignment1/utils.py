import random

def make_sudoku_pair(r, k):
    # Makes a 1-D list of the two sudokus from a model solution by reversing the hash
    s = []
    for i in range(k**2):
        for j in range(k**2):
            for x in range(k**2):
                if r[(x) * (k**4) + (0) * (k**6) + (i) * (k**2) + (j)]>0 :
                    s.append(x+1)
                    break
    for i in range(k**2):
        for j in range(k**2):
            for x in range(k**2):
                if r[(x) * (k**4) + (1) * (k**6) + (i) * (k**2) + (j)]>0 :
                    s.append(x+1)
                    break
    return s

def make_sudoku(r, k):
    # Makes a 1D list of a single sudoku from a model solution by reversing the hash
    s = []
    for i in range(k**2):
        for j in range(k**2):
            for x in range(k**2):
                if r[(x) * (k**4) + (0) * (k**6) + (i) * (k**2) + (j)]>0 :
                    s.append(x+1)
                    break
    return s

def randomise_sudoku(s1, k):
    # Fills either (exclusively) a row, column, or a box of sudoku s1, with a random permutation of numbers in the range [1,k**2]
    temp = []
    for i in range(k**2):
        temp.append(1+i)
    
    random.shuffle(temp)


    n = random.randint(1,3)
    y = random.randint(0, (k**2) - 1)

    if(n == 1):
        for j in range(k**2):
            s1[y][j] = temp[j]
    elif(n == 2):
        for j in range(k**2):
            s1[j][y] = temp[j]
    else:
        for i in range(k):
            for j in range(k):
                s1[(y//k)*k+i][(y%k)*k+j] = temp[i*k+j]
    return s1



