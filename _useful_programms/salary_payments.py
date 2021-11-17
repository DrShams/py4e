#1)in this section we assign how many hours we actually work including all overtime which should be payed separately with definetely bonus
hrs_employee = input("How many hours per month you actually work per month?\n Please input total sum of time including overtime:\t\t\t\t") #45 or 228(fact)
try:
    h_employee = int(hrs_employee)
except:
    print("Error, please enter hours as numbers (ex. '228',\n where '228' - hours which you really work)")
    quit()

#2)in this section we assign how many hours we should work according to our contract
hrs_employer = input("How many hours per month your employer pay you for?: \n Please input total sum of time according to your contract with employer:\t") #40 or 171(fact)
try:
    h_employer = int(hrs_employer)
except:
    print("Error, please enter hours as numbers (ex. '228',\n where '228' - hours which you really work)")
    quit()

#3)in this section we assign how much the employer should pay for the time according to our contract
rate = input("How much your employer pay you for 1 hour?:\t\t\t\t\t") #10.5 or 175(fact in roubles)
try:
    r = float(rate)
except:
    print("Error, please enter rate as float (ex. '175.0',\n where '175.0' - amount of roubles which you gain for 1 hour of your work)")
    quit()

#4)in this section we assign how much the employer should pay for every hour overtime according to our contract
bonus = input("What is the bonus for 1 hour overtime?\n Please enter the float value ex. 1.2 - 2.0):\t\t\t\t\t") #10.5 or 175(fact in roubles)
try:
    rate_b = float(bonus)
except:
    print("Error, please enter bonus as float (ex. '1.5',\n where '1.5' - the amount which should be normally multiplied by your rate")
    quit()

#5)make calculation of total sum of our salary
def computepay(h_employee,h_employer):
    if h_employee <= h_employer:
        return (r*h)
    else:
        return (r*h_employer+(h_employee-h_employer)*rate_b*r)

print("Pay",computepay(h_employee,h_employer))
