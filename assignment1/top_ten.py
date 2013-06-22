import sys
import json

def lines(fp):
    print str(len(fp.readlines()))

def tweethashs(sf):
	hash_list =[]
	hashtags = {}
	for line in sf:
		res = json.loads(line)
		if "entities" in res.keys():
			for k in res["entities"]["hashtags"]:
				if k["text"].encode("utf-8") in hashtags:
					hashtags[k["text"].encode("utf-8")] += 1
				else:
					hashtags[k["text"].encode("utf-8")] = 1
					#hash_list.append(k["text"].encode("utf-8"))

	return hashtags

def main():
	tweet_file = open(sys.argv[1])
	hashtags = tweethashs(tweet_file)
	keys = hashtags.keys()
	keys.sort(lambda x,y: cmp(hashtags[x], hashtags[y]), reverse=True)
	i = 0
	for k in keys:
		if i < 10:
			print k,'\t',hashtags[k]
			i += 1
		else:
			break

	tweet_file.close()	


if __name__ == '__main__':
    main()