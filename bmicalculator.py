height=float(input("Please enter your height"))
weight=int(input("Please enter your weight"))
bmi=weight/float(height*height)

if bmi<18.5:
    print("Underweight")
if bmi>=18.5 and bmi<25:
    print("Normal Weight")
if bmi>=25 and bmi<30:
    print("Overweight")

