height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
bmi = round(weight)/ float(height) ** 2
if bmi <18.5 :
    print(f"Your bmi is{bmi}, you are underweight. ")
elif bmi <25:
    print(f"Your bmi is{bmi},you have normal weight")
elif bmi >25 :
    print(f"Your bmi is{bmi}, you are slighty overweight")
elif bmi > 30:
    print(f"Your bmi is{bmi}, you are obese")
else: 
    print(f"Your bmi is{bmi},you are clinically obese")    
