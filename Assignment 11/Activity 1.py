# This program returns the days in a month of a corresponding year
# References
# https://www.youtube.com/watch?v=6a39OjkCN5I&ab_channel=Telusko


month_names = ['January', 'February', 'March', 'April', 'May', 'June', 
               'July', 'August', 'September', 'October', 'November', 'December']
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def get_year():
    print("please enter a year: ")
    year = int(input())
    return year


def month_num():
    print("please enter a month (1-12): ")
    month = int(input())
    return month


def calculate_days(year, month):
    if month == 2 and (year % 4 == 0 and year % 100 != 0 or year% 400 == 0):
        days = 29
        return days
    else:
        days = days_in_month[month - 1]
        return days
    

def display_output(days, month, year):
    print(f"{month_names[month-1]} {year} has {days} days")


def main():
    year = get_year()
    month = month_num()
    days = calculate_days(year, month)
    display_output(days, month, year)

    
main()
