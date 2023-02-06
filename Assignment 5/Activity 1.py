
def calculateAnnualPay(wP):
    annualPay = wP * 52
    
    return annualPay

def calculateMonthlyPay(wP):
    monthlyPay = wP * 4
    
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
# This program will calculate someones age in months, days, hours, seconds.
years = Get_Age()
AgeMonths = Calculate_Age_Months(years)
AgeDays = Calculate_Age_Days(years) 
AgeHours = Calculate_Age_Hours(AgeDays)
AgeSeconds = Calculate_Age_Seconds(AgeHours)
Display_Results(AgeMonths, AgeDays, AgeHours, AgeSeconds)
