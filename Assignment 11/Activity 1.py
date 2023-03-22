# This program returns the days in a month of a certain year
# References
# https://www.youtube.com/watch?v=6a39OjkCN5I&ab_channel=Telusko


def get_year():
    print("Please enter a year: ")
    year = int(input())
    return year


def get_month():
    while True:
        print("Please enter a month (1-12): ")
        month = int(input())
        if month < 1 or month > 12:
            print(f"{month} is an invalid input.") 
        else:
            return month
    

def get_month_name(month):
    month_names = ['January', 'February', 'March', 
        'April', 'May', 'June', 
        'July', 'August', 'September', 
        'October', 'November', 'December']

    if month < 1 or month > 12:
        return None
    
    return month_names[month - 1]


def get_month_days(year, month):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month < 1 or month > 12:
        return None

    if calculate_leap_year(year):
        days_in_month[1] = 29
    
    return days_in_month[month - 1]


def calculate_leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False


def display_output(month, days, year):
    print(f"{month} {year} has {days} days.")


def main():
    year = get_year()
    month = get_month()
    month_name = get_month_name(month)
    month_days = get_month_days(year, month)
    display_output(month_name, month_days, year)
    

main() 
