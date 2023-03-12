# This program will guess a number that the user is thinking of
# Reference:
# https://www.youtube.com/watch?v=M3zmcj8sNu8&ab_channel=GeekTutorials


low = 0
high = 100
guesses = 0


def ask_for_number():
    input("think of a number bewteen 1 and 100, then press enter to continue...")

    
def number_guess():
    global low, high, guesses
    while True:
        mid = (low + high) // 2
        response  = input("is your number " + str(mid) + "? (high /low/equal)")
        guesses += 1
        if response == 'high':
            low = mid + 1
        elif response == 'low':
            high = mid - 1
        else:
            return guesses


def display_output(guesses):
    print("I guessed your number in " + str(guesses) + " guesses!")


def main():
    ask_for_number()
    guesses = number_guess()
    display_output(guesses)


main()
