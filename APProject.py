import random

def diceRoll():
 return random.randint (1,6) + random.randint(1,6)

def rollNum():
 global list    # cycles through every number spits out how many times each number got rolled
 cycle = 2
 per = 0
 while cycle <= 12:
  non = 0
  for i in range(len(list)):
   if list[i] == cycle:
    non += 1
    per = (non / len(list)) * 100
  print ("Out of " + (str(len(list)) + " rolls, " + (str(cycle)) + " rolled " + str(non) + " times or "+ (str(round(per, 2))) + " percent of the time." ))
  cycle += 1
   

list = []
L = 0
numsim = int(input("How many simulations do you want to run?"))

while L < numsim:
 list.append(diceRoll()) #function called inside loop, input determines amount of sims
 L += 1

print(rollNum())
