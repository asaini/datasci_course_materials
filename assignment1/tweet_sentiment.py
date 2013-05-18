import sys, json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))


class Tweet:
    
    def __init__(self, tweet):
        self.tweet = tweet
    
    @classmethod
    def getTweetsFromFile(cls, tweet_file):
        for line in tweet_file:
            tweet = json.loads(line)
            try:
                text = tweet['text']
                yield Tweet(tweet)
            except KeyError:
                continue
    
    @property
    def text(self):
        return self.tweet['text']
        

class TweetProcessor:
    
    def __init__(self, sent_file):
        self.sentiments = self._getSentimentsFromFile(sent_file)
            
    def _getSentimentsFromFile(self, sent_file):
    	sentiments = {}
    	for line in sent_file:
    		word, sent = line.split('\t')
    		sentiments[word] = float(sent)
    	return sentiments

    def computeSentiment(self, tweet):
        text = tweet.text
        text = text.lower()
        tokens = text.split()

        score = 0
        for token in tokens:
            try:
                score += self.sentiments[token]
            except KeyError:
                continue

        return score

	
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    
    tp = TweetProcessor(sent_file)
    tweets = Tweet.getTweetsFromFile(tweet_file)
    
    for tweet in tweets:
        sentScore = tp.computeSentiment(tweet)
        print '%f' % (sentScore)
		

if __name__ == '__main__':
    main()
