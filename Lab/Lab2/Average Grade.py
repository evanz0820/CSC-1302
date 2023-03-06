avg = 0

try:
    aliceGrade = int(input("What is Alice's grade? "))
    guyGrade = int(input("What is Guy's grade? "))

    avg = (aliceGrade + guyGrade) / 2
    
    if (aliceGrade < 0 or guyGrade < 0):
        raise ValueError
    
except ValueError:
    avg = 0
    print("Invalid value. Please try again")

except ZeroDivisionError:
    print("You can't divide by zero ")

finally:
    print("The average grade is", avg)