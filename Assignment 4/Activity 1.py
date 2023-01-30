# This program will calculate weekly, monthly, and annual pay
# References:
# https://www.youtube.com/watch?v=1BB1sCkS9oU

print("Enter hours wokred per week:")
Hours_worked_per_week = float(input())
print("Enter rate per hour")
Rate_per_hour = float(input())
Weekly_pay = Hours_worked_per_week * Rate_per_hour
Monthly_pay = Weekly_pay * 4
Annual_pay = Monthly_pay * 12
print("$" + str(Weekly_pay) + " per week")
print("$" + str(Monthly_pay) + " per month")
print("$" + str(Annual_pay) + " annually")
