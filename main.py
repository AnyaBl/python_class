import math

n = float(input("Enter the amount of km the car can drive per day: "))
m = float(input("Enter the amount of total km per route: "))

result_route = math.ceil(m/n)

print( "Amount of days needed for your car to finish the route is: ",  result_route)


