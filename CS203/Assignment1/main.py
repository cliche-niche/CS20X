import random
import matplotlib.pyplot as plt

# Taking input
m = int(input("Enter the value of m: "))
assert m>0, "m should be positive."

p = input("Enter the value of p_i's (in a single line): ").split()
p = list(map(float, p))
assert len(p)==m, "Length of <p> does not match the value of m."
for x in p:
    assert x>0, "probabilities should be positive"
    assert x<1, "probabilities should be lesser than 1"
assert abs(sum(p)-1)<1e-3, "Sum of probabilities should be 1"

n = int(input("Enter the value of n: "))
assert n>0, "n should be positive"

# Converting p to a cumulative distribution
for i in range(1, m):
    p[i] += p[i-1]

# Returns a number from [0,m) corresponding to a given number in [0,1] using the cumulative distribution
def pick(choice, p):
    for i in range(len(p)):
        if i==len(p)-1 or p[i]>=choice:
            return i

# Returns the sum of all X_i in a sample
def sampling(p, n):
    s = 0
    for _ in range(n):
        choice = random.uniform(0, 1)
        s += pick(choice, p)
    return s

# Iterations
epochs = random.randint(1e4, 11e3)
results = []
for _ in range(epochs):
    s = sampling(p, n)
    results.append(round(s/n, 1))

# Preparing data for plotting the graphs.
count = {}
for r in results:
    count[r] = count.get(r, 0) + 1

x, y, z = [], [], []
for c in count:
    z.append([c, count[c]])

z = sorted(z)
for i in z:
    x.append(i[0])
    y.append(i[1])

filename = "200057_m"+str(m)+"_n"+str(n)+"_e"+str(epochs)+".png"
plt.plot(x, y, c='red')
plt.savefig(filename) # Saving the plot
plt.show()