# This program will calculate someones age in months, days, hours, seconds.
#References: https://www.youtube.com/watch?v=AWek49wXGzI


def calculate_months(years):
    age_months = years * 12

    return age_months


def calculate_days(years):
    age_days = years * 365

    return age_days


def calculate_hours(age_days):
    age_hours = age_days * 24

    return age_hours


def calculate_seconds(age_hours):
    age_seconds = age_hours * 3600

    return age_seconds


def get_age():
    print("Please enter your age in years: ")
    years = float(input())

    return years

def get_unit():
    print("Would you like your age in (M)onths,(D)ays,(H)ours,(S)econds?")
    unit = str(input())
    
    return unit


def display_results(years,unit,age_months,age_days,age_hours,age_seconds):
    if unit == "M":
        print(str(age_months) + " Months Old")
    elif unit == "D":
        print(str(age_days) + " Days old")
    elif unit == "H":
        print(str(age_hours) + " Hours old")
    elif unit == "S":
        print(str(age_seconds) + " Seconds old")
    else:
        return None
    
    
def main():
    years = get_age()
    unit = get_unit()
    age_months = calculate_months(years)
    age_days = calculate_days(years)
    age_hours = calculate_hours(age_days)
    age_seconds = calculate_seconds(age_hours)
    display_results(years,unit,age_months,age_days,age_hours,age_seconds)


main()
