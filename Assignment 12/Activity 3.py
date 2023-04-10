# This program will guess a number that the user is thinking of
# References:
# https://www.youtube.com/watch?v=M3zmcj8sNu8&ab_channel=GeekTutorials
# https://www.youtube.com/watch?v=z_M7a291pvE&t=18s&ab_channel=HackersRealm
# https://chat.openai.com


def get_response(guess):
    response = input(f"Is your number {guess}? (h/l/e) ")
    return response


def process_guess():
    low = 0
    high = 100
    guesses = []
    while True:
        guess = (low + high) // 2
        guesses.append(guess)
        response = get_response(guess)
        if response == 'h':
            low = guess + 1
        elif response == 'l':
            high = guess - 1
        else:
            return guesses


def display_output(guesses):
    print(', '.join(map(str, guesses)))


def main():
    print("Think of a number between 1 and 100...")
    guesses = process_guess()
    display_output(guesses)


main()
