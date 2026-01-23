def convert (grade):
    if int(grade) >= 90:
        return ("A") 
    elif int(grade) >= 80 and int(grade) < 90:
        return("B")
    elif int(grade) >= 70 and int(grade) < 80:
        return ("C")
    elif int(grade)>= 60 and int(grade) < 70:
        return ("D")
    elif int(grade) < 60:
        return ("F")
    
grade = input ("What is your grade? ") 


print ("Your letter grade is " + str(convert(grade)))





