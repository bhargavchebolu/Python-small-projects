height = float(input("What is your height in m: "))
weight = float(input("What is your weight in kg: "))
bmi = weight/(height * height)

if (bmi <= 18.5 ):
    print("Eat more, you are underweight")
elif (bmi >18.5 or bmi <=24.9):
       print("You have normal weight")
elif (bmi >24.9 or bmi<=29.9 ):
       print("Have a diet, you are overweight")
else:
    print("OMG! You have Obesity")
