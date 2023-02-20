# This program generates a list of multiplication expressions for a given value
# References:
# https://www.youtube.com/watch?v=dHANJ4l6fwA


def get_value():
    print("Please enter a value: ")
    value = float(input())
    return value


def get_amount():
    print("please eneter the number of expressions you would like: ")
    amount = float(input())
    return amount


def main():
    value = get_value()
    amount = get_amount()
   


    for i in range(1,int(amount) + 1):
        result = value * i
        print(value, "*", i, "=", result)


main()
