def CalculateAgeMonths(years):
    AgeMonths = years * 12

    return AgeMonths

def CalculateAgeDays(years):
    AgeDays = years * 365

    return AgeDays

def CalculateAgeHours(AgeDays):
    AgeHours = AgeDays * 24

    return AgeHours

def CalculateAgeSeconds(AgeHours):
    AgeSeconds = AgeHours * 3600

    return AgeSeconds

def GetAge():
    print("Please enter your age in years: ")
    years = float(input())

    return years

def DisplayResults(AgeMonths,AgeDays,AgeHours,AgeSeconds):
    print( str(AgeMonths) + " Months old")
    print( str(AgeDays) + " Days old")
    print( str(AgeHours) + " Hours old")
    print( str(AgeSeconds) + " Seconds old")





# Main
# This program will calculate someones age in months, days, hours, seconds.
years = GetAge()
AgeMonths = CalculateAgeMonths(years)
AgeDays = CalculateAgeDays(years) 
AgeHours = CalculateAgeHours(AgeDays)
AgeSeconds = CalculateAgeSeconds(AgeHours)
DisplayResults(AgeMonths,AgeDays,AgeHours,AgeSeconds)
