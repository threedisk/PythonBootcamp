print("Welcome to Head or Tails Randomization")

# Import Random Module
import random

random_headtails = random.randint(0,1)
print(random_headtails)
if (random_headtails==1):
    print("Heads")
else:
    print("Tails")
