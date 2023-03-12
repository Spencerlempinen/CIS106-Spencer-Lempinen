# This program will guess a number that the user is thinking of
# Reference:
# https://www.youtube.com/watch?v=M3zmcj8sNu8&ab_channel=GeekTutorials


def ask_for_number():
    return input("Think of a number between 1 and 100, then press Enter to continue...")


def process_guess(low, high, guesses):
    while True:
        mid = (low + high) // 2
        response = input("Is your number " + str(mid) + "? ([h]igh/[l]ow/[e]qual)")
        guesses += 1
        if response == 'h':
            low = mid + 1
        elif response == 'l':
            high = mid - 1
        else:
            return guesses


def display_output(guesses):
    print("I guessed your number in " + str(guesses) + " guesses!")


def main():
    low = 0
    high = 100
    guesses = 0
    ask_for_number()
    guesses = process_guess(low, high, guesses)
    display_output(guesses)
    
    
main()
