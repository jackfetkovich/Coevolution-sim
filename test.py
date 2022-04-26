import random

host_pop_A = 2000
host_pop_a = 100

parasite_pop_A = 10
parasite_pop_a = 90

for i in range (25):
  host_pop = host_pop_A + host_pop_a
  parasite_pop = parasite_pop_A + parasite_pop_a
  
  # Adjusting Host A Population
  host_pop_A = host_pop_A - (parasite_pop_A / parasite_pop)*random.randint(50, 200)

  print("********")
  print(f"Generation {i}")
  print(f"Host Population: {host_pop_A + host_pop_a}")
  print(f"\tPercent A: {host_pop_A /(host_pop_a + host_pop_A) * 100}")
  print(f"\tPercent a: {host_pop_a /(host_pop_a + host_pop_A) * 100}")
  # print(f"Parasite Population: {parasite_pop_A + parasite_pop_a}")
  # print(f"\tPercent A: {parasite_pop_A /(parasite_pop_a + parasite_pop_A) * 100}")
  # print(f"\tPercent a: {parasite_pop_a /(parasite_pop_a + parasite_pop_A) * 100}")



