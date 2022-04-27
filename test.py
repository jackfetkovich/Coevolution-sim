import random
import matplotlib.pyplot as plt
import numpy as np

host_pop_A = 2000
host_pop_a = 100
dhAdt = 1.001

parasite_pop_A = 1500
parasite_pop_a = 200
# dhadt = random.uniform(0.97, 1.01)
dhadt = 1.01


print(dhadt)

# x=[0,1]
# y=[host_pop_A, host_pop_A * dhAdt]
y2=[parasite_pop_A, parasite_pop_A * dhadt]
y=[]
x=[]
y2=[]



dhAdt_list = [dhAdt]
dhadt_list = [dhadt]

host_pop_A = host_pop_A * dhAdt
parasite_pop_A = parasite_pop_A * dhadt


# for i in range (125):
#   x.append(i+2)
#   if(dhadt_list[i] - dhadt_list[i-1] > 0):
#     dhAdt = dhAdt * 0.99 * (1 + random.uniform(0,0))
#   else:
#     dhAdt = dhAdt * 1.001 * (1 + random.uniform(0,0))
  
#   host_pop_A = host_pop_A * dhAdt
#   dhAdt_list.append(dhAdt)

#   if host_pop_A < 100:
#     host_pop_A += 50
#     dhAdt += 0.5
  

#   if(dhAdt_list[i] - dhAdt_list [i-1] > 0.2 ):
#     dhadt = dhadt * 1.03 *(1 + random.uniform(0,0))
#   else:
#     dhadt = dhadt * 0.99 *(1 + random.uniform(0,0))
#   parasite_pop_A = parasite_pop_A * dhadt
#   dhadt_list.append(dhadt)

#   if parasite_pop_A < 1:
#     parasite_pop_A += 100
#     dhadt = 1.5

#   y.append(host_pop_A)
#   y2.append(parasite_pop_A)

for i in range (125):
  x.append(i)
  y.append(np.sin(i/4) + 1)
  y2.append(0.8*np.sin((i-6)/4)-0.3 + 1)


print(y)
print(y2)
fig, ax = plt.subplots()

ax.plot(x, y, y2, linewidth=2.0)

plt.show()



