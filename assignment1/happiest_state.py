import sys
import json

def readSentiment(file):
    scores = {} # initialize an empty dictionary
    for line in file:
        term, score = line.split("\t") # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score) # Convert the score to an integer.

    return scores

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sent_scores = readSentiment(sent_file)
    state_score = {}

    for line in tweet_file:
        res = json.loads(line)
        if res.get('place'):
            place = res.get('place')
            if(place.get('country') == "United States"):
                state = place.get('full_name').split(',')[1].strip()
                if state in state_score:
                    state_score[state] = state_score[state] + computeSentiment(res.get('text'), sent_scores)
                else:
                    state_score[state] = computeSentiment(res.get('text'), sent_scores)
    
    print sorted(state_score, key=state_score.get, reverse=True)[0]
    

def computeSentiment(tweet, sent_scores):
    if tweet is None:
        return 0

    score = 0
    words = tweet.split(' ')
    for word in words:
        if word in sent_scores:
            score += sent_scores[word]

    return score

if __name__ == '__main__':
    main()