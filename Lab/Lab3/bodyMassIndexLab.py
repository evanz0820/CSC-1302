meter = float(input("What is your height? "))
kg = float(input("What is your weight? "))

def bodyMassIndex (height, weight):
    try:
        if (meter < 0 or kg < 0):
            raise ValueError

        bmi = (weight)/(height**2)

    except ValueError:
        bmi = 0
        print("Invalid Input. Please try again")

    finally:
        print("Your BMI is ", bmi)

bodyMassIndex(meter, kg)