name = input("What's your name? ")
height_m = input("What's your height? ")
weight_kg = input("What's your weight? ")

bmi = weight_kg / (height_m ** 2)
print("BMI: ")
print(bmi)

if bmi < 25:
    print(name)
    print("is not overweight!")
else:
    print(name)
    print("is overweight!")