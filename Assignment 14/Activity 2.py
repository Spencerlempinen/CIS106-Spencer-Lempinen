# this program will average a set of scores from a .txt file
# references:
# https://www.youtube.com/watch?v=XPO6ITK2Ecc&ab_channel=ProgrammingGuru
 

 def read_scores(filename):
    scores = []
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()[1:]
            if not lines:
                print("Error: empty file")
                return None
            for line in lines:
                score = parse_score(line)
                if score is None:
                    print("Error: missing or bad data")
                    return None
                scores.append(score)
            return scores
    except FileNotFoundError:
        print(f"Error: {filename} not found")
        return None


def parse_score(line):
    fields = line.strip().split(',')
    if len(fields) != 2:
        return None
    name, score = fields
    try:
        score = int(score)
    except ValueError:
        return None
    return score


def calculate_high_score(scores):
    if not scores:
        return None
    return max(scores)


def calculate_low_score(scores):
    if not scores:
        return None
    return min(scores)


def calculate_average_score(scores):
    if not scores:
        return None
    return round(sum(scores) / len(scores), 2)


def display_scores(scores, high, low, average):
    print("Scores:")
    for score in scores:
        print(score)
    print(f"Highest score: {high}")
    print(f"Lowest score: {low}")
    print(f"Average score: {average}")


def main():
    filename = "scores.txt"
    scores = read_scores(filename)
    if scores is not None:
        high = calculate_high_score(scores)
        low = calculate_low_score(scores)
        average = calculate_average_score(scores)
        display_scores(scores, high, low, average)


main()
