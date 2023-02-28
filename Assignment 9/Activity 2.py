#This Program will ask the user for a specified amount of test score and average them
#References:
#https://www.youtube.com/watch?v=DdsxsW3UUX0&ab_channel=CodingwithChapa

def get_amount():
    print("Please eneter how many score you would like to average: ")
    amount = int(input())
    return amount


def get_scores(amount):
    thesum = 0
    count = 0
    while count < amount:
        score = float(input("please enter a score: "))
        thesum += score
        count += 1
    average = thesum / amount
    return average
    


def display_output(average):
    print("The average is: " + str(average))


def main():
    amount = get_amount()
    average = get_scores(amount)
    display_output(average)


main()
