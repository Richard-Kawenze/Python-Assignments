#RICHARD KAWENZE MUNYWOKI
#SCT211-0053/2022

from datetime import date, datetime

name=input("Please Enter your name ")
print("Welcome "+name+" to Simple Calculator ")
print("Operations")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5. Calculate your Age")
choice=input("Select the operation you wish to perform ")
choice=int(choice)

if choice==1:
    number1=int(input("Enter your first number "))
    number2=int(input("Enter your second number "))
    sum=number1+number2
    print("The sum of the two numbers is ",sum)
elif choice==2:
    number1=int(input("Enter your first number "))
    number2=int(input("Enter your second number "))
    minus=number1-number2
    print("The result of the subtraction is ",minus)
elif choice==3:
     number1=int(input("Enter your first number "))
     number2=int(input("Enter your second number "))
     multiple=number1*number2
     print("The result is ",multiple)
elif choice==4:
     number1=int(input("Enter your first number "))
     print("The second number should not be a zero")
     number2=int(input("Enter your second number "))
     divident=number1/number2
     print("The result of the operation is ",divident)
elif choice==5:
     year=int(input("Enter your year of Birth " ))
     month=int(input("Enter your month of Birth "))
     birthdate=int(input("Enter date of Birth "))

     dateOfBirth=date(year,month,birthdate)
     today=date.today()
     age=today.year-dateOfBirth.year
     ageMonths=age*12
     ageDays=age*365

     print("Your Age in Years is ", age)
     print("Your Age in Months is ", ageMonths)
     print("Your age in Days is ",ageDays)

else:
     print("Please try again")
     print("Enter number between one and five")


                