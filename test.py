import random
import matplotlib.pyplot as plt
import numpy as np

host_pop_A = 2000
host_pop_a = 100
dhAdt = 1.001

parasite_pop_A = 1500
parasite_pop_a = 200
dhadt = random.uniform(0.97, 1.01)

print(dhadt)

x=[0,1]
y=[host_pop_A, host_pop_A * dhAdt]
y2=[parasite_pop_A, parasite_pop_A * dhadt]

host_pop_A = host_pop_A * dhAdt
parasite_pop_A = parasite_pop_A * dhadt


for i in range (100):
  x.append(i+2)
  if(dhadt - dhAdt > 0.02):
    dhAdt = dhAdt * 0.99 * (1 + random.uniform(-0.05, 0.05))
  else:
    dhAdt = dhAdt * 1.001 * (1 + random.uniform(-0.05, 0.05))
  
  host_pop_A = host_pop_A * dhAdt

  if(dhAdt - dhadt > 0.0):
    dhadt = dhadt * 1.01
  else:
    dhadt = dhadt * 0.99
  parasite_pop_A = parasite_pop_A * dhadt



  y.append(host_pop_A)
  y2.append(parasite_pop_A)



fig, ax = plt.subplots()

ax.plot(x, y, y2, linewidth=2.0)

plt.show()



