import math
entered_year=int(input("Enter the year: "))
first_condition = entered_year%4
second_condition = entered_year%100
third_condition = entered_year%400

if first_condition == 0 and second_condition !=0 or third_condition==0:
    print("It is a leap year")
else:
    print("It is not  a leap year ")
