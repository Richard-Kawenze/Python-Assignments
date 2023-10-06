#RICHARD MUNYWOKI KAWENZE
#SCT211-0053/2022

year=int(input("Enter the year"))
if(year%4==0 and year%100 or year%400==0):
    print("This is a leap year")
else:
    print("The year is not a leap year")