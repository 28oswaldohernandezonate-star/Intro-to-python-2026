import random

def diceRoll():
 return random.randint (1,6) + random.randint(1,6)


def rollNum(Rolls): 
 cycle = 2
 per = 0
 while cycle <= 12:
  non = 0
  for i in range(len(Rolls)):
   if Rolls[i] == cycle:
    non += 1
    per = (non / len(Rolls)) * 100
  print("Out of " + (str(len(Rolls)) + " rolls, " + (str(cycle)) + " rolled " + str(non) + " times or "+ (str(round(per, 2))) + " percent of the time." ))
  cycle += 1
   

Rolls = []
L = 0
numsim = int(input("How many simulations do you want to run?"))

while L < numsim:
 Rolls.append(diceRoll())
 L += 1


rollNum(Rolls)

