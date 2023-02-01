def calculateAnnualPay(wP):
    annualPay = wP * 52
    
    return annualPay

def calculateMonthlyPay(wP):
    monthlyPay = wP * 4
    
    return monthlyPay

def calculateWeeklyPay(hours, rate):
    weeklyPay = rate * hours
    
    return weeklyPay

# Main
hours = float(input("Enter the number of hours worked per week: "))
rate = float(input("Enter the rate per hour: "))

wP = calculateWeeklyPay(hours, rate)
print("$" + str(wP) + " per week")

mP = calculateMonthlyPay(wP)
print("$" + str(mP) + " per month")

aP = calculateAnnualPay(wP)
print("$" + str(aP) + " annually")

