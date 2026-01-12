num1 = float(input("Type in your first number > "))
num2 = float(input("Type in your second number > "))
print("Type in 1 for additon, 2 for subtraction, 3 for multiplication, 4 for division, 5 for exponents, and 6 for long division.")
choice = input("Select Operation -> ")
if choice == "1":
   print(num1+num2)

elif choice == "2": 
   print(num1-num2)

elif choice == "3":
   print(num1*num2)

elif choice == "4":
   print(num1/num2)

elif choice == "5":
   print(num1**num2)

elif choice == "6":
  print(divmod(num1, num2))
