weight=float(input("Enter your weight in kg."))
height=float(input("Enter your height in feet."))

pounds=(weight*2.2)
feet=(height/3.28)

bmi=round(pounds/feet**2)

if bmi <18.5:
    print(f"Your BMI is {bmi},you are underweight.")
elif bmi <30:
    print(f"Your BMI is {bmi},you are overweight.")
elif bmi <35:
    print(f"Your BMI is {bmi},you are obese.")
else:
    print(f"Your BMI is {bmi},you are clinically obese.")
