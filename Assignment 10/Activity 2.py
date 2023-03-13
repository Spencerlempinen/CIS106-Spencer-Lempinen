# This program will guess a number that the user is thinking of
# References:
# https://www.youtube.com/watch?v=M3zmcj8sNu8&ab_channel=GeekTutorials


def guess_number(low, high):
    return (low + high) // 2


def process_guess():
    low = 0
    high = 100
    guess_count = 0

    while True:
        guess = guess_number(low, high)
        response = input("Is your number " + str(guess) + "? (h/l/e)")
        guess_count += 1
        if response == 'h':
            low = guess + 1
        elif response == 'l':
            high = guess - 1
        else:
            return guess_count


def display_output(guesses):
    print("I guessed your number in " + str(guesses) + " guesses!")


def main():
    print("Think of a number between 1 and 100...")
    guesses = process_guess()
    display_output(guesses)


main()
