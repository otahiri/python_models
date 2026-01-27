import sys


def main():
    scores = []
    print("=== Player Score Analytics ===")
    count = len(sys.argv)
    if count < 2:
        print("No scores provided. Usage: python3 ft_score_analytics.py \
<score1> <score2> ...")
        return
    else:
        try:
            scores = [int(score) for score in sys.argv[1:]]
        except ValueError:
            print("Error user entered an invalid score the score should be \
a valid integer")
            return
        print(f"Scores processed: {str(scores)}")
        print(f"Total players: {count - 1}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {(sum(scores) / (count - 1)):.1f}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    main()
