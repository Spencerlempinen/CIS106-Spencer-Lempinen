# This program Will return users high low and average test score
# References
# https://www.youtube.com/watch?v=6a39OjkCN5I&ab_channel=Telusko


def get_amount():
    print("Please enter how many scores you would like to average: ")
    amount = int(input())
    return amount


def get_score():
    print("Please enter a score: ")
    score = float(input())
    return score


def calculate_average(amount, scores):
    thesum = 0
    for score in scores:
        thesum += score
    average = thesum / amount
    return scores, average
    

def display_output(scores, average):
    high_score = max(scores)
    low_score = min(scores)
    print("The high score is:", high_score)
    print("The low score is:", low_score)
    print("The average score is:", average)


def main():
    amount = get_amount()
    scores = [0] * amount  
    for i in range(amount):
        scores[i] = get_score()  
    scores, average = calculate_average(amount, scores)
    display_output(scores, average)


main()
