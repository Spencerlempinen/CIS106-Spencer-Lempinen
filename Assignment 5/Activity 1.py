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
print("Enter hours worked per week: ")
hours = int(input())
print("Enter rate of pay: ")
rate = int(input())
wP = calculateWeeklyPay(hours, rate)
print("$" + str(wP) + " per week")
mP = calculateMonthlyPay(wP)
print("$" + str(mP) + " per month")
aP = calculateAnnualPay(wP)
print("$" + str(aP) + " annually")


