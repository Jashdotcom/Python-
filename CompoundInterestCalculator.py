import math


principal_bal = 0
roi = 0
time_period = 0

while(principal_bal <=0):
    principal_bal = float(input("Enter the intial principal balance ($) : "))
    if principal_bal<=0:
        print("Principal balance should be greater than zero!")
    
while(roi <=0):
    roi = float(input("Enter the rate of interest (%) : "))
    if roi<=0 :
        print("ROI should be greater than zero!")

while(time_period<=0):
    time_period = float(input("Enter the time period (in years) :"))
    if time_period<=0:
        print("Time period should be greater than zero!")

final_amount = principal_bal * pow((1 + roi/100),time_period)
print("")
print(f"Balance after {time_period} years at {roi}% rate will be ${final_amount:,.2f}")