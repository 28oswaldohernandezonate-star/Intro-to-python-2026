import random 

WinNum = 0
Nowin = 0 
loop = 0
Sw = 0
while loop != 100:
 wDoor = random.randint(1,3)
 Ppick = random.randint(1,3)
 Rdoor = random.randint(1,3)

 while Rdoor == wDoor or Rdoor == Ppick:
  Rdoor = random.randint(1,3)


 print("W " + str(wDoor) + " P " + str(Ppick) + " R " + str(Rdoor))

 Switch = random.randint(1,3) 

 while Switch == Rdoor:
   Switch = random.randint(1,3) 
 if Switch == Ppick:
   Switch = wDoor

 if Switch == wDoor:
    WinNum += 1
    loop += 1
 else:
    Nowin += 1
    loop += 1

print ("# of win is " + str(WinNum))
print ("# of loss is " + str(Nowin))


