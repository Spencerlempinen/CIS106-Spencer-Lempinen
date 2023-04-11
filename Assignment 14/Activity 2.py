# this program will average a set of scores from a .txt file
# references:
# https://www.youtube.com/watch?v=XPO6ITK2Ecc&ab_channel=ProgrammingGuru
 

def read_scores(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()[1:]
            scores = []
            for line in lines:
                name, score = line.strip().split(',')
                scores.append(int(score))
            return scores
    except FileNotFoundError:
        print(f"Error: file {filename} not found.")
        return None


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
    display_scores(scores)


main()
