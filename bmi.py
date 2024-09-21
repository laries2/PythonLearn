name = "Bett"
height = 5.6
weight = 59
bmi = height / (height**2)
if bmi < 25:
    print(name)
    print(bmi)
    print("Is not overweight")
else:
    print(name)
    print("Is overweight")