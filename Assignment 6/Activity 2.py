# This program will calculate someones age in months, days, hours, seconds.


def calculate_months(years):
    months = years * 12
    return months


def calculate_days(years):
    days = years * 365
    return days


def calculate_hours(days):
    hours = days * 24
    return hours


def calculate_seconds(hours):
    seconds = hours * 60 * 60
    return seconds


def get_age():
    print("Please enter your age in years: ")
    years = float(input())
    return years


def display_results(months, days, hours, seconds):
    print(str(months) + " Months old")
    print(str(days) + " Days old")
    print(str(hours) + " Hours old")
    print(str(seconds) + " Seconds old")
   
    
def main():
    years = get_age()
    months = calculate_months(years)
    days = calculate_days(years)
    hours = calculate_hours(days)
    seconds = calculate_seconds(hours)
    display_results(months, days, hours, seconds)


main()
