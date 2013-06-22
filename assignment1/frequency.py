import sys
import json

def lines(fp):
    print str(len(fp.readlines()))

def tweetterms(sf):
	word_list =[]
	for line in sf:
		res = json.loads(line)
		if "text" in res.keys():
			tweet = res["text"].encode('utf-8')
			word_list += tweet.strip().split()

	return word_list

def wordcount(wordlist):
	frequency = {}
	for w in wordlist:
		frequency[w] = wordlist.count(w)
	return frequency


def main():
	tweet_file = open(sys.argv[1])
	word_list = tweetterms(tweet_file)
	frequency = wordcount(word_list)
	for key in frequency:
		frequency[key] = (frequency[key])/float(len(word_list))
		#print key.strip() + " " + str(frequency[key])
		print key + '\t' + frequency[key]
	tweet_file.close()	


if __name__ == '__main__':
    main()
