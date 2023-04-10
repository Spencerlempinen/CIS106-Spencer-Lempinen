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
