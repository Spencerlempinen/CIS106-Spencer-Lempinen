def scroll_text():
    text = input("Enter a line of text: ")
    num_chars = int(input("Enter the number of characters per line: "))
    num_lines = int(input("Enter the number of lines to print: "))
    direction = input("Enter the scroll direction (left or right): ")
    return text, num_chars, num_lines, direction
    

def process_text(text, num_chars, num_lines, direction):
    num_repeats = (num_chars // len(text)) + 2
    repeated_text = text * num_repeats
    lines = []
    for i in range(num_lines):
        line_text = repeated_text[i*num_chars:(i+1)*num_chars]
        if len(line_text) < num_chars:
            line_text += repeated_text[(i+1)*num_chars:(i+2)*num_chars-len(line_text)]
        if direction == "right":
            line_text = line_text[-1] + line_text[:-1]
        elif direction == "left":
            line_text = line_text[1:] + line_text[0]
        else:
            print("Invalid direction.")
            return
        lines.append(line_text)
    return lines


def output_lines(lines):
    for line in lines:
        print(line)

def main():
    text, num_chars, num_lines, direction = scroll_text()
    lines = process_text(text, num_chars, num_lines, direction)
    output_lines(lines)

main()
