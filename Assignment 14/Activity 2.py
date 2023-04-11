# this program will average a set of scores from a .txt file
# references:
# https://www.youtube.com/watch?v=XPO6ITK2Ecc&ab_channel=ProgrammingGuru
 

def read_scores(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()[1:]
            if not lines:
                print("Error: file is empty.")
                return None
            return process_scores(lines)
    except FileNotFoundError:
        print(f"Error: file {filename} not found.")
        return None


def process_scores(lines):
    scores = []
    for line in lines:
        fields = line.strip().split(',')
        if len(fields) != 2:
            print("Error: missing or bad data.")
            return None
        name, score = fields
        try:
            score = int(score)
        except ValueError:
            print("Error: missing or bad data.")
            return None
        scores.append(score)
    return scores


def display_scores(scores):
    if scores is None:
        return
    print("Scores:")
    for score in scores:
        print(score)
    print("Highest score:", max(scores))
    print("Lowest score:", min(scores))
    avg_score = sum(scores) / len(scores)
    print("Average score: {:.2f}".format(avg_score))


def main():
    filename = "scores.txt"
    scores = read_scores(filename)
    if scores is not None:
        display_scores(scores)


main()
