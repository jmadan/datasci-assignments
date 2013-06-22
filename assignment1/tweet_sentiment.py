import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def readsentiments(sf):
    scores = {} # initialize an empty dictionary
    for line in sf:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    return scores
    #print scores.items() # Print every (term, score) pair in the dictionary    


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sentiments_scores = readsentiments(sent_file)
    for line in tweet_file:
    	res = json.loads(line)
    	if "text" in res.keys():
    		tweet = res["text"].encode('utf-8')
    		tweet_score = 0
    		for key in sentiments_scores:
    			if tweet.find(key) > 0:
    				tweet_score = tweet_score + sentiments_scores[key]
    	print str(tweet_score)
    tweet_file.close()	
    #lines(sent_file)
    #lines(tweet_file)
    #pyresponse = json.load(tweet_file.readlines())
    #print pyresponse

if __name__ == '__main__':
    main()
