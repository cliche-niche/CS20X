import random
import matplotlib.pyplot as plt

for _ in range(3):
    n = random.randint(1e4, 1e6)
    k_array = list(range(1, 1001))
    n_mean_array, n_median_array = [], [] # Store the calculated value of N according to Mean and Median respectively

    n_tickets = [] # Stores the k tickets drawn out
    for k in range(1, 1001):
        n_tickets.append(random.randint(1, n))
        n_tickets.sort() # Useful for finding the Median
        n_mean_array.append((sum(n_tickets)/len(n_tickets))*2-1)
        n_median_array.append(n_tickets[k//2]*2-1 if k%2==1 else (n_tickets[k//2]+n_tickets[k//2-1])-1)

    # Plotting the graph
    plt.style.use('dark_background')
    plt.figure(figsize=(8,6))
    plt.plot(k_array, n_median_array, color = 'cyan', label = 'Median')
    plt.plot(k_array, n_mean_array, color = 'tomato', label = 'Mean')
    plt.axhline(y = n, color = 'violet', label = "N=" + str(n))
    plt.legend(loc = "upper right")
    plt.xlabel("k")
    plt.ylabel("Calculated N~" )
    filename = "200057_n_" + str(n) + ".png"
    plt.savefig(filename, dpi=400) # Saving the plots
    plt.show()