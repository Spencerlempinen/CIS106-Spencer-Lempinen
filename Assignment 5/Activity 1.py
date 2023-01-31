def calculate_pay(hours,rate):
    weekly_pay = hours * rate
    monthly_pay = weekly_pay * 4 
    annual_pay = weekly_pay * 52 
    return weekly_pay, monthly_pay, annual_pay

print("Enter hours worked per week: ")
hours = float(input())

print("Enter rate of pay: ")
rate = float(input())

weekly_pay, monthly_pay, annual_pay = calculate_pay(hours,rate)

print(weekly_pay)
print(monthly_pay)
print(annual_pay)
