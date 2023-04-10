# this program will parse a list of strings
# References:
# https://www.youtube.com/watch?v=aQJlsmTGExc&ab_channel=MasterCodeOnline
# https://www.youtube.com/watch?v=sCnWxZUhiTQ&ab_channel=RussellLewis
# https://www.youtube.com/watch?v=k9TUPpGqYTo&ab_channel=CoreySchafer
# github co-pilot


def get_input():
    line = input("Enter a line of comma-separated-values: ")
    return line


def process_line(line):
    items = line.split(",")
    return [item.strip() for item in items]


def print_items(items):
    for item in items:
        print(item)


def main():
    line = get_input()
    items = process_line(line)
    print_items(items)


main()
