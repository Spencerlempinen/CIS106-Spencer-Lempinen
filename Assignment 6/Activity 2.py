def Calculate_Age_Months(years):
    AgeMonths = years * 12

    return AgeMonths

def Calculate_Age_Days(years):
    AgeDays = years * 365

    return AgeDays

def Calculate_Age_Hours(AgeDays):
    AgeHours = AgeDays * 24

    return AgeHours

def Calculate_Age_Seconds(AgeHours):
    AgeSeconds = AgeHours * 3600

    return AgeSeconds

def Get_Age():
    print("Please enter your age in years: ")
    years = float(input())

    return years

def Display_Results(AgeMonths, AgeDays, AgeHours, AgeSeconds)
    print( str(AgeMonths) + " Months old")
    print( str(AgeDays) + " Days old")
    print( str(AgeHours) + " Hours old")
    print( str(AgeSeconds) + " Seconds old")

# Main
# This program will calculate someones age in months, days, hours, seconds.
years = Get_Age()
AgeMonths = Calculate_Age_Months(years)
AgeDays = Calculate_Age_Days(years) 
AgeHours = Calculate_Age_Hours(AgeDays)
AgeSeconds = Calculate_Age_Seconds(AgeHours)
Display_Results(AgeMonths, AgeDays, AgeHours, AgeSeconds)

