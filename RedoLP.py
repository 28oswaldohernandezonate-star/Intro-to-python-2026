def itsPrime(Ldigit):
    for i in range(2, Ldigit):
     if Ldigit % i == 0:
       return False
    return True
    
numDigits = input ()
Ldigit = ("")
for i in range(int(numDigits)):
  Ldigit = Ldigit + "9"
Ldigit = int(Ldigit)

while not itsPrime(Ldigit):
  Ldigit = Ldigit - 1 
else: 
 print (str(Ldigit) + " is largest prime") 

