# This Program will average test scores privided by user
# References:
# https://www.youtube.com/watch?v=DdsxsW3UUX0&ab_channel=CodingwithChapa


def get_amount():
    print("Please eneter how many scores you would like to average: ")
    amount = int(input())
    return amount


def get_score():
    print("please enter a score: ")
    score = float(input())
    return score


def calculate_average(amount):
    sum = 0
    count = 0
    while count < amount:
        score = get_score()
        sum += score
        count += 1
    average = sum / amount
    return average
    

def display_output(average):
    print("The average is: " + str(average) + "%")


def main():
    amount = get_amount()
    average = calculate_average(amount)
    display_output(average)


main()
