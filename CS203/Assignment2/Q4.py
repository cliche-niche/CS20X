import random
import matplotlib.pyplot as plt

def create_dnf(n):
    dnf = []
    for _ in range(n):
        clause = []
        for __ in range(n-4):
            x = (random.randint(0,1)*2-1)*(random.randint(1, n))
            clause.append(x)
        dnf.append(clause)
    return dnf

def try_solve(dnf):
    n = len(dnf)
    m = 4*n
    sols = 0
    for _ in range(m):
        sol = []
        for i in range(1, n+1):
            sol.append(i*(2*(random.randint(0,1))-1))
        if check_sol(dnf, sol):
            sols += 1
    return sols

def solve(dnf, solution):
    if len(dnf) == len(solution):
        return 1 if check_sol(dnf, solution) else 0
    else:
        return solve(dnf, solution+[len(solution)+1]) + solve(dnf, solution+[-len(solution)-1])

def check_sol(dnf, sol):
    for clause in dnf:
        for cube in clause:
            if cube not in sol:
                break
        else:
            return True
    return False

n_array = [6, 8, 10, 12]
esti, actu = [], []
for n in n_array:
    dnf = create_dnf(n)
    sols = try_solve(dnf)
    esti.append(sols*(2**n)/(4*n))
    actual_sols = solve(dnf, [])
    actu.append(actual_sols)

plt.style.use('dark_background')
plt.plot(n_array, esti, 'cyan', label='Estimate')
plt.plot(n_array, actu, 'tomato', label='Actual')
plt.legend(loc='lower right')
plt.xlabel('n')
plt.ylabel('Solutions')
plt.show()