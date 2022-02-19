def add_cell(asmp, i, j, s, x, k):
    # Adds assumptions corresponding to an alraedy filled cell

    # Assumes 0-based indexing for s, i, j. For eg., the range [0,k**2-1) is expected for i, j
    # Assumes x to be in the range [0, k**2], but hashed only for x>0

    a_sxij = (k**6)*(s) + (k**2)*(i) + (j) + (1) # (k**6)*(s) + (k**4)*(x-1) + (k**2)*(i) + (j) + (1)
    pres = 1

    if x!=0:
        for num in range(0, k**2):
            if num+1==x:
                pres=1
            else:
                pres=-1
            asmp.append((num*(k**4) + a_sxij) * (pres))

def cell_clause(s, k):
    # Adds clauses corresponding to a cell
    clauses = []
    
    for i in range(k**2):
        for j in range(k**2):
            single_clause = []
            a_sxij = (k**6)*(s) + (k**2)*(i) + (j) + (1)
            
            # At least one number in each cell
            for num1 in range(0, k**2):
                single_clause.append((num1)*(k**4) + a_sxij)
            clauses.append(single_clause)

            # At most one number in each cell
            for num1 in range(0, k**2):
                for num2 in range(num1+1, k**2):
                    single = []
                    single.append(-((num1)*(k**4) + a_sxij))
                    single.append(-((num2)*(k**4) + a_sxij))
                    clauses.append(single)

    return clauses

def cell_diff(i, j, x1, x2, k):
    # Adds clauses for different values in same cell, i.e., S1[i,j] != S2[i,j]
    clauses = []

    a_x1 = (i) * (k**2) + (j) + (1)
    a_x2 = (k**6) + (i) * (k**2) + (j) + (1)

    if(x1 and x2):
        x1 = x1-1
        x2 = x2-1
        single_clause = []
        single_clause.append(-(a_x1 + x1 * (k**4)))
        single_clause.append(-(a_x2 + x1 * (k**4)))
        clauses.append(single_clause)
        single_clause = []
        single_clause.append(-(a_x1 + x2 * (k**4)))
        single_clause.append(-(a_x2 + x2 * (k**4)))
        clauses.append(single_clause)
    elif(x1>0):
        x1 = x1-1
        single_clause = []
        single_clause.append(-(a_x1 + x1 * (k**4)))
        single_clause.append(-(a_x2 + x1 * (k**4)))
        clauses.append(single_clause)
    elif(x2>0):
        x2 = x2-1
        single_clause = []
        single_clause.append(-(a_x1 + x2 * (k**4)))
        single_clause.append(-(a_x2 + x2 * (k**4)))
        clauses.append(single_clause)
    else:
        for x in range(k**2):
            single_clause = []
            single_clause.append(-(a_x1 + x * (k**4)))
            single_clause.append(-(a_x2 + x * (k**4)))
            clauses.append(single_clause)

    return clauses

def add_rows(s, k):
    # Adds clauses for each row in the s-th sudoku
    clauses = []

    for i in range(k**2):
        for x in range(k**2):
            single_clause = []
            for j in range(k**2):
                # At least one x in each row
                a_sxij = (x) * (k**4) + (s) * (k**6) + (i) * (k**2) + (j) + (1)
                single_clause.append(a_sxij)

                # Redundancy #1
                # At most one x in each row
                for j0 in range (j+1, k**2):
                    single = []
                    single.append(-a_sxij)
                    single.append(-(a_sxij-j+j0))
                    clauses.append(single)
            
            clauses.append(single_clause)
    
    return clauses

def add_cols(s, k):
    # Adds clauses corresponding to each column in the s-th sudoku
    clauses = []

    for j in range(k**2):
        for x in range(k**2):
            single_clause = []
            for i in range(k**2):
                # At most one x in each column
                a_sxij = (x) * (k**4) + (s) * (k**6) + (i) * (k**2) + (j) + (1)
                single_clause.append(a_sxij)

                # Redundancy #2
                # At most one x in each column
                for i0 in range (i+1, k**2):
                    single = []
                    single.append(-a_sxij)
                    single.append(-(a_sxij + (i0-i) * (k**2)))
                    clauses.append(single)
            
            clauses.append(single_clause)
            
    return clauses

def add_box(s, k):
    # Adds clauses for each box in the s-th sudoku
    clauses = []

    for x in range(k**2):
        for n in range(k):
            for m in range(k):
                single_clause = []
                for i in range(k):
                    for j in range(k):
                        # At least one x in each box
                        a_sxij = (x) * (k**4) + (s) * (k**6) + (n*k+i) * (k**2) + (m*k+j) + (1)
                        single_clause.append(a_sxij)

                        # Redundancy #3
                        # At most one x in each box
                        for i0 in range(i+1, k):
                            for j0 in range(j+1, k):
                                single = []
                                single.append(-a_sxij)
                                single.append(-(a_sxij + (i0-i) * (k**2) + (j0-j)))
                                clauses.append(single)

                clauses.append(single_clause)

    return clauses
