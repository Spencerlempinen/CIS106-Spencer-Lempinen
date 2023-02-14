# This program will calculate someones age in months, days, hours, seconds.
# References: 
# https://www.youtube.com/watch?v=AWek49wXGzI


def calculate_months(years):
    age_months = years * 12
    return age_months


def calculate_days(years):
    age_days = years * 365
    return age_days


def calculate_hours(years):
    age_hours = years * 365 * 24
    return age_hours


def calculate_seconds(years):
    age_seconds = years * 365 * 24 * 3600
    return age_seconds


def get_age():
    print("Please enter your age in years: ")
    years = float(input())
    return years


def get_unit():
    print("Would you like your age in (M)onths, (D)ays, (H)ours, (S)econds?")
    unit = input()
    return unit


def display_results(results, label):
    print(f"{results}  {label} Old")

        
def main():
    years = get_age()
    unit = get_unit()
    if unit == "M":
        age_months = calculate_months(years)
        display_results(age_months, "Months")
    elif unit == "D":
        age_days = calculate_days(years)
        display_results(age_days, "Days")
    elif unit == "H":
        age_hours = calculate_hours(years)
        display_results(age_hours, "Hours")
    elif unit == "S":
        age_seconds = calculate_seconds(years)
        display_results(age_seconds, "Seconds")
    else:
        display_results("Invalid input")
        

main()
