import string

def get_profanity_score(text, slurs):
    words = text.translate(str.maketrans('', '', string.punctuation)).lower().split()
    profanity_score = 0
    for word in words:
        if word in slurs:
            profanity_score += 1
    return profanity_score

def read_slurs(file_path):
    with open(file_path, 'r') as file:
        slurs = file.read().splitlines()
    return slurs

def get_tweet_profanity_scores(tweet_file_path, slurs_file_path):
    slurs = read_slurs(slurs_file_path)
    profanity_scores = {}
    with open(tweet_file_path, 'r') as file:
        for line in file:
            profanity_scores[line] = get_profanity_score(line, slurs)
    return profanity_scores

def main():
    tweet_file_path = 'tweets.txt'
    slurs_file_path = 'slurs.txt'
    profanity_scores = get_tweet_profanity_scores(tweet_file_path, slurs_file_path)
    for tweet, score in profanity_scores.items():
        print(f'{tweet}: {score}')

if __name__ == '__main__':
    main()
