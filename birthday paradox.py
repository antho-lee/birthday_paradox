import matplotlib.pyplot as plt
import numpy as np

x = np.array([])
y = np.array([])

previous = 0
highest_gradiant = 0
highest_gradiant_at = 0
g = np.array([])

for n in range(50):
    product = 1
    denominator = 1

    for i in range(n):
        product *= 366-n
        denominator *= 365

# calculate the probability of >= 2 person having same birthday among n people.
    output = (1 - product/denominator)*100

# Find the rigorous growth point
    g= np.append(g,output-previous)
    if(g[n] > highest_gradiant):
        highest_gradiant = g[n]
        highest_gradiant_at = n
    previous = output

# Record data for graphing later
    x = np.append(x, n)
    y = np.append(y, output)

# Print result
    print(n, end="   ")
    print(output, end="")
    print("%   ", g[n])

print("\nmost rigorous growth at:", highest_gradiant_at)
print(highest_gradiant, "%")

# graphing
plt.plot(x,y)
plt.scatter(highest_gradiant_at,y[highest_gradiant_at])
# plt.plot(x,g) # for gradiant graph.
# plt.scatter(highest_gradiant_at,highest_gradiant)
plt.show()

