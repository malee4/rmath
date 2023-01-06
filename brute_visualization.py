import matplotlib.pyplot as plt
import numpy as np
from tools import *

# for two-candidate 
iter = 1_000
a_values = []
b_values = []

for i in range(iter):
    a = np.random.random()
    b = np.random.random()

    candidates = [a, b]
    output = perform_instant_runoff(candidates, 2)
    if output:
        a_values.append(a)
        b_values.append(b)

plt.scatter(a_values, b_values)
plt.show()

