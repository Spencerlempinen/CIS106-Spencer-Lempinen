# This Program will take a user specified amount of test scores and average them
# References:
# https://www.youtube.com/watch?v=DdsxsW3UUX0&ab_channel=CodingwithChapa


def get_amount():
    print("Please eneter how many score you would like to average: ")
    amount = int(input())
    return amount


def get_score():
    print("please enter a score: ")
    score = float(input())
    return score


def calculate_average(amount):
    thesum = 0
    count = 0
    while count < amount:
        score = get_score()
        thesum += score
        count += 1
    average = thesum / amount
    return average
    

def display_output(average):
    print("The average is: " + str(average) + "%")


def main():
    amount = get_amount()
    average = calculate_average(amount)
    display_output(average)


main()

