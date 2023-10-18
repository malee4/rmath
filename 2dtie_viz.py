import matplotlib.pyplot as plt
import numpy as np
from tools import perform_instant_runoff
from polarized import polarized_perform_instant_runoff
from loss import loss_perform_instant_runoff

is_polarized = False
is_loss = False
# for two-candidate 
iter = 1_000_000
a_values = []
b_values = []

for i in range(iter):
    a = np.random.random()
    b = np.random.random()

    candidates = [a, b]
    if is_polarized:
        output = polarized_perform_instant_runoff(candidates, 2)
    elif is_loss:
        output = loss_perform_instant_runoff(candidates, 2)
    else:
        output = perform_instant_runoff(candidates, 2)
    if output:
        a_values.append(a)
        b_values.append(b)

plt.scatter(a_values, b_values)
if is_polarized:
    plt.title('Locations of Tie for Two Candidates, Polarized')
else:
    plt.title('Locations of Tie for Two Candidates')
plt.xlabel('A')
plt.ylabel('B')