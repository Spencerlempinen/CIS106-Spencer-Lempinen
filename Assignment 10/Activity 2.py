# This program will guess a number that the user is thinking of
# Reference:
# https://www.youtube.com/watch?v=M3zmcj8sNu8&ab_channel=GeekTutorials


def get_user_input():
    return input("Think of a number between 1 and 100, then press Enter to continue...")


def process_guess():
    low = 0
    high = 100
    guesses = 0
    
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


def display_output(num_guesses):
    print("I guessed your number in " + str(num_guesses) + " guesses!")


def main():
    get_user_input()
    num_guesses = process_guess()
    display_output(num_guesses)


main()
