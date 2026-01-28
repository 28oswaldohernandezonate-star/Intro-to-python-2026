amount = input("How many items are you adding to list? >")

list = []

for i in range (int(amount)):
 inp = input("What are you adding to list? >")
 list.append(inp)

for item in list:
  print (item, end = ' ')


