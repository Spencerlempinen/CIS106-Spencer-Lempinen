def calculateAnnualPay(weeklyPay):
    annualPay = weeklyPay * 52
    
    return annualPay

def calculateMonthlyPay(weeklyPay):
    monthlyPay = weeklyPay * 4
    
    return monthlyPay

def calculateWeeklyPay(hours, rate):
    weeklyPay = rate * hours
    
    return weeklyPay

def displayResults(weeklyPay, monthlyPay, annualPay):
    print("$" + str(weeklyPay) + " Per week")
    print("$" + str(monthlyPay) + " Per month")
    print("$" + str(annualPay) + " Annually")

def getHours():
    print("Enter hours worked: ")
    localHours = float(input())
    
    return localHours

def getRate():
    print("Enter rate per hour: ")
    rate = float(input())
    
    return rate

# Main
# This Program Will calculate Weekly,Monthly,and Annual Pay.
hours = getHours()
rate = getRate()
weeklyPay = calculateWeeklyPay(hours, rate)
monthlyPay = calculateMonthlyPay(weeklyPay)
annualPay = calculateAnnualPay(weeklyPay)
displayResults(weeklyPay, monthlyPay, annualPay)
