meter = float(input("What is your height? "))
kg = float(input("What is your weight? "))

def bodyMassIndex (height, weight):
    bmi = (weight)/(height**2)

    print("Your BMI is ", bmi)

bodyMassIndex(meter, kg)