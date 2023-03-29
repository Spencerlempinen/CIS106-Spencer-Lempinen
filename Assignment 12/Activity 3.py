# This program will guess a number that the user is thinking of
# References:
# https://www.youtube.com/watch?v=M3zmcj8sNu8&ab_channel=GeekTutorials
# https://www.youtube.com/watch?v=z_M7a291pvE&t=18s&ab_channel=HackersRealm


def guess_number(low, high):
    return (low + high) // 2


def process_guess():
    low = 0
    high = 100
    guess_count = []
    while True:
        guess = guess_number(low, high)
        response = input(f"Is your number {guess}? (h/l/e) ")
        guess_count.append(guess)
        if response == 'h':
            low = guess + 1
        elif response == 'l':
            high = guess - 1
        else:
            return guess_count


def display_output(guesses):
    for i, guess in enumerate(guesses):
        print(f"{i+1}. {guess}")


def main():
    print("Think of a number between 1 and 100...")
    guesses = process_guess()
    display_output(guesses)


main()
