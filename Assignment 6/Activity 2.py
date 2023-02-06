def calculate_age_months(years):
    age_months = years * 12

    return age_months


def calculate_age_days(years):
    age_days = years * 365

    return age_days


def calculate_age_hours(age_days):
    age_hours = age_days * 24

    return age_hours


def calculate_age_seconds(age_hours):
    age_seconds = age_hours * 3600

    return age_seconds


def get_age():
    print("Please enter your age in years: ")
    years = float(input())

    return years


def display_results(age_months, age_days, age_hours, age_seconds):
    print(str(age_months) + " Months old")
    print(str(age_days) + " Days old")
    print(str(age_hours) + " Hours old")
    print(str(age_seconds) + " Seconds old")


# Main
# This program will calculate someones age in months, days, hours, seconds.
years = get_age()
age_months = calculate_age_months(years)
age_days = calculate_age_days(years)
age_hours = calculate_age_hours(age_days)
age_seconds = calculate_age_seconds(age_hours)
display_results(age_months, age_days, age_hours, age_seconds)
