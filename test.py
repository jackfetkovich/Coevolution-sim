from sys import argv

import random
import matplotlib.pyplot as plt
import numpy as np

# 1/3, 8/3, 4, 1

ALPHA = 1/3  # Coefficient of host growth
BETA = 8/3  # Coefficient of predation
DELTA = 4  # Coefficient of parasite growth
GAMMA = 1  # Coefficient of death of parasites

dhdt = 0
dpdt = 0


def update_differentials(host_pop, parasite_pop):
  global dhdt
  global dpdt

  dhdt = ALPHA * host_pop - BETA * host_pop * parasite_pop
  dpdt = DELTA * host_pop * parasite_pop - GAMMA * parasite_pop


host_pop = 0
parasite_pop = 0

generations = 0

if(len(argv) < 4):
  generations = 150
else:
  generations = int(argv[3])

if(len(argv) < 3):
  parasite_pop = 0.2
else:
  parasite_pop = float(argv[2])

if(len(argv) < 2):
  host_pop = 0.8
else:
  host_pop = float(argv[1])


# 0.8, 0.2
# host_pop = 0.3
# parasite_pop = 0.4

update_differentials(host_pop, parasite_pop)

x = [0, 1]
y = [host_pop, host_pop * dhdt]
y2 = [parasite_pop, parasite_pop * dpdt]

host_pop = max(0, min(1, host_pop + host_pop*dhdt))
parasite_pop = max(0, min(1, parasite_pop + parasite_pop*dpdt))

for i in range(generations):
  x.append(i+2)
  update_differentials(host_pop, parasite_pop)

  host_pop = max(0, min(1, host_pop + host_pop*dhdt))
  parasite_pop = max(0, min(1, parasite_pop + parasite_pop*dpdt))

  y.append(host_pop)
  y2.append(parasite_pop)
  print(dhdt)


fig, ax = plt.subplots()

ax.plot(x, y, y2, linewidth=2.0)

plt.show()
