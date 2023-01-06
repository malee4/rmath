import matplotlib.pyplot as plt
import numpy as np
from tools import *

# for two-candidate 
iter = 100_000
a_values = []
b_values = []
c_values = []

for i in range(iter):
    a = np.random.random()
    b = np.random.random()
    c = np.random.random()

    candidates = [a, b]
    output = perform_instant_runoff(candidates, 2)
    if output:
        a_values.append(a)
        b_values.append(b)
        c_values.append(c)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# ax.set_title('Points of Tie for 3D')
ax.set_xlabel('A')
ax.set_ylabel('B')
ax.set_zlabel('C')

ax.scatter(a_values, b_values, c_values)
plt.show()

