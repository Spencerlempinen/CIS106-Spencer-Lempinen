# this program will average a set of scores from a .txt file
# references:
# https://www.youtube.com/watch?v=XPO6ITK2Ecc&ab_channel=ProgrammingGuru
 

def read_scores(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()[1:]
            if not lines:
                Errors('empty_file')
                return None
            scores = process_scores(lines)
            if scores is None:
                Errors('bad_data')
                return None
            return scores
    except FileNotFoundError:
        Errors('no_file', filename=filename)
        return None


def process_scores(lines):
    scores = []
    for line in lines:
        fields = line.strip().split(',')
        if len(fields) != 2:
            return None
        name, score = fields
        try:
            score = int(score)
        except ValueError:
            return None
        scores.append(score)
    return scores


def Errors(error_type, filename=None):
    if error_type == 'bad_data':
        print("Error: missing or bad data.")
    elif error_type == 'empty_file':
        print("Error: file is empty.")
    elif error_type == 'no_file':
        print(f"Error: file {filename} not found.")


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
    filename = "empty.txt"
    scores = read_scores(filename)
    if scores is not None:
        display_scores(scores)


main()
