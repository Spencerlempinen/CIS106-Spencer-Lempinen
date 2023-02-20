# This program generates a list of multiplication expressions for a given value
# References:
# https://www.youtube.com/watch?v=dHANJ4l6fwA


def get_value():
    print("Please enter a value: ")
    value = float(input())
    return value


def get_amount():
    print("please eneter the number of expressions you would like: ")
    amount = int(input())
    return amount


def generate_expressions(amount, value):
    expressions = []
    for i in range(1, amount + 1):
        result = value * i
        expression = f"{value} * {i} = {result}"
        expressions.append(expression)
    return expressions


def display_output(expressions):
    print("here are the multiplication expressions: ")
    for expression in expressions:
        print(expression)    


def main():
    value = get_value()
    amount = get_amount()
    expressions = generate_expressions(amount, value)
    display_output(expressions)


main()
