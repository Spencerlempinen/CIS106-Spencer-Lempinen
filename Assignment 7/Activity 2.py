# This program will calculate someones age in months, days, hours, seconds.


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

def get_unit():
    print("Would you like your age in Months, Days, Hours, Seconds, or all 4?")
    unit = str(input())
    
    return unit


def display_results(years,unit,age_months, age_days, age_hours, age_seconds):
    if unit == "Months":
        return str(age_months) + " Months old"
    elif unit == "Days":
        return str(age_days) + " Days old"
    elif unit == "Hours":
        return str(age_hours) + " Hours old"
    elif unit == "Seconds":
        return str(age_seconds) + " Seconds old"
    elif unit == "all 4":
        return (
            str(age_months) + " Months old",
            str(age_days) + " Days old",
            str(age_hours) + " Hours old",
            str(age_seconds) + " Seconds old" 
        )
    else:
        return None
    
    
def main():
    years = get_age()
    unit = get_unit()
    age_months = calculate_age_months(years)
    age_days = calculate_age_days(years)
    age_hours = calculate_age_hours(age_days)
    age_seconds = calculate_age_seconds(age_hours)
    result = display_results(years,unit,age_months, age_days, age_hours, age_seconds)
    

    if unit == "all 4":
        print(result[0])
        print(result[1])
        print(result[2])
        print(result[3])
    else:
        print(result)


main()
