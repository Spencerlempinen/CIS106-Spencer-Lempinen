# This program will calculate weekly, monthly, and annual pay
# References:
# https://www.youtube.com/watch?v=1BB1sCkS9oU

print("Enter hours wokred per week:")
hours_worked_per_week = float(input())

print("Enter rate per hour")
rate_per_hour = float(input())

weekly_pay = hours_worked_per_week * rate_per_hour
monthly_pay = weekly_pay * 4
annual_pay = weekly_pay * 52

print("$" + str(weekly_pay) + " per week")
print("$" + str(monthly_pay) + " per month")
print("$" + str(annual_pay) + " annually")
