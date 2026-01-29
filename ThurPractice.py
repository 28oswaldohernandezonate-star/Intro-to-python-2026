ExList = [1, 15, 9, 11, 4, 13, 57, 81, 6, 8, 0]



def N (ExList):
    ExList = [1, 15, 9, 11, 4, 13, 57, 81, 6, 8, 0]
    for i in range(len(ExList)):
        if ExList[i] < 0:
          return False
    return True
        
print (N(ExList))


def L (ExList):
    ExList = [1, 15, 9, 11, 4, 13, 57, 81, 6, 8, 0] 
    largest = ExList[0] 
    for i in range(len(ExList)): 
      if ExList[i] > largest:
            largest = ExList[i]
    return largest

print (L(ExList))



def H (ExList):
    ExList = [1, 15, 9, 11, 4, 13, 57, 81, 6, 8, 0]
    for i in range(len(ExList)): 
        ExList[i] = ExList[i] * 100
    return ExList

print (H(ExList))

def R (ExList):
   ExList = [1, 15, 9, 11, 4, 13, 57, 81, 6, 8, 0] 
   Hold = ExList[0]
   for i in range(len(ExList)-1):
       ExList[i] = ExList[i+1]
   ExList[-1] = Hold
   return ExList

print (R(ExList))
       
       



    
        
