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

def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	sentiments_scores = readsentiments(sent_file)
	terms = {}
	for line in tweet_file:
		res = json.loads(line)
		if "text" in res.keys():
			tweet = res["text"].encode('utf-8')
			temp_terms = tweet.split()
			tweet_score = 0
			for key in sentiments_scores:
				for w in temp_terms:
					if w == key:
						temp_terms.remove(w)
						tweet_score += sentiments_scores[key]
					terms[w] = tweet_score
	for z in terms:
		print z + " " + str(terms[z])
	tweet_file.close()	


if __name__ == '__main__':
    main()
