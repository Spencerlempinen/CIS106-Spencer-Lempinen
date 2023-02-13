# this prgram will calculate users weekly, monthly, and annual apy
# References:
# https://www.youtube.com/watch?v=AWek49wXGzI

def get_hours():
    print("Enter hours worked")
    hours = float(input())
    return hours


def get_rate():
    print("Enter your rate of pay")
    rate = float(input())
    return rate


def calculate_weekly(hours, rate):
    if hours <= 40:
       weekly = hours * rate
       return weekly
    else:
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * (rate * 1.5)
        regular_pay = 40 * rate
        weekly = regular_pay + overtime_pay
        return weekly

    
def calculate_monthly(weekly):
    monthly_pay = weekly * 4
    return monthly_pay


def calculate_annual(weekly):
    annual = weekly * 52
    return annual


def display_results(weekly, monthly, annual):
    print("$" + str(weekly) + " Per week")
    print("$" + str(monthly) + " Per month")
    print("$" + str(annual) + " Annually")


def main():
    hours = get_hours()
    rate = get_rate()
    weekly = calculate_weekly(hours, rate)
    monthly = calculate_monthly(weekly)
    annual = calculate_annual(weekly)
    display_results(weekly, monthly, annual)


main()
