import matplotlib.pyplot as plt
import numpy as np
from tools import perform_instant_runoff
from polarized import polarized_perform_instant_runoff
from loss import loss_perform_instant_runoff

is_polarized = False
is_loss = True

# for two-candidate 
iter = 1_000_00
a_values = []
b_values = []
c_values = []

for i in range(iter):
    a = np.random.random()
    b = np.random.random()
    c = np.random.random()

    candidates = [a, b, c]
    if is_polarized:
        output = polarized_perform_instant_runoff(candidates, 2)
    elif is_loss:
        output = loss_perform_instant_runoff(candidates, 2)
    else:
        output = perform_instant_runoff(candidates, 2)

    if output:
        a_values.append(a)
        b_values.append(b)
        c_values.append(c)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

if is_polarized:
    ax.set_title('Points of Tie for 3D, Polarized')
else:
    ax.set_title('Points of Tie for 3D')
ax.set_xlabel('A')
ax.set_ylabel('B')
ax.set_zlabel('C')

ax.scatter(a_values, b_values, c_values)
plt.show()

