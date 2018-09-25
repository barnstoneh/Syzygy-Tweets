import tweepy
import csv
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import TweetTokenizer
import re
from textblob import TextBlob
from decimal import *
import operator
import json

consumer_key = "Cr0bjqLGriMZG3TnFBzCBzGFx"
consumer_secret = "xRhT6k99CxmccOhOGG0OYQYYaxHQPJDWIffgDvi4DeMScaTxIw"
access_token = "920101378894254080-8GFgtsqKA2m44BQR0QPGyEoT4Evj0IU"
access_token_secret = "jbWenfOcMOAhjsq9Or55orzx9Z8EOOR7KdbFK1MLORENj"


#The following method downloads Syzgy's tweets and stoes them in a csv file.
#Paremeter = screen_name - refers to the twitter screen name that you wish to dowload tweets from.
# The following code is credited to: https://gist.github.com/yanofsky/5436496
def get_all_tweets(screen_name):
    #Twitter only allows access to a users most recent 3240 tweets with this method
    
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)
	
	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)
	
	#save most recent tweets
	alltweets.extend(new_tweets)
	
	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1
	
	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		print "getting tweets before %s" % (oldest)
		
		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		
		#save most recent tweets
		alltweets.extend(new_tweets)
		
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		
		print "...%s tweets downloaded so far" % (len(alltweets))
	
	#transform the tweepy tweets into a 2D array that will populate the csv	
	outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
	
	#write the csv	
	with open('%s_tweets.csv' % screen_name, 'wb') as f:
		writer = csv.writer(f)
		writer.writerow(["id","created_at","text"])
		writer.writerows(outtweets)
	
	pass


#Prints a unigram frequency table, the number of words (including numbers) and the number of unique words (including numbers).
def word_Tokenize():
    
    print ('hikhkjhkjkjh')
    file = 'SyzTweets.txt'
    f = (open(file, 'rU')).read()  
    nltk.sent_tokenize(f)
    tokenizer = TweetTokenizer()
    #word_text = nltk.word_tokenize(f)
    word_text = tokenizer.tokenize(f)
    for line in word_text:
        ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", line).split())
    wordFreq = {}
    #Gets rid of all characters I do not want included in word_text
    word_text = [e for e in word_text if e !=',','.''(',')',':',';','!','\\','s','https',"'","-",'_',"?","d9","d9_","d9___","d9__","9_","/","s","aa","st","c8","b4","\'8","u143","uc0","ce","d5","db_","fc","95","d3"]
    numWords = len(word_text)
    for i in range(0, numWords):
        word = word_text[i]
        word = word.lower()
        word = word.strip()
        if wordFreq.has_key(word) == False:
            wordFreq.update({word:1})
        else:
            curVal = wordFreq.get(word, None)
            newVal = curVal + 1
            wordFreq.update({word:newVal})
            
    d_view = [ (v,k) for k,v in wordFreq.iteritems() ]
    d_view.sort(reverse=True) # sorts in order of greatest key value and then alphabeticly
    d_view = [ (v,k) for k,v in wordFreq.iteritems() ]
    d_view.sort(reverse=True)
    
    numWords = sum(wordFreq.values())    
    numUniqueWords = len(wordFreq) # number of unique words

    print "Number of Words (including numbers):", numWords
    print "Number of Unique words (including numbers):", numUniqueWords    
    print "Bellow is a frequency rank (unigram) for all of the uniqe words in the text file:"
    for v,k in d_view:
        print "%s: %d" % (k,v)
        
        
#Prints a bigram frequency table
def bigram():
    myBigram = []
    myDict = {}
    sent_text= nltk.sent_tokenize('SyzygyNgramTweets.txt')
    with open('SyzygyNgramTweets.txt') as f:
        #print("hi")
        #For sent in nltk.sent_tokenize(f):
        for line in f:
            
            #line = 
            ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", line).split())
            tokenizer = TweetTokenizer()
            #word_text = nltk.word_tokenize(f)
            sent_text = tokenizer.tokenize(line)
            #sent_text = nltk.word_tokenize(line)
            size = len(sent_text) 
            for i in range(0, size-1):
                if i+1 > size:
                    break
                word = sent_text[i] + ", " + sent_text[i+1]
            
               #myBigram.append(word)
               # print(myBigram)
                word = word.lower()
                word = word.strip()
                if myDict.has_key(word) == False:
                    myDict.update({word: 1})
                else:
                    curVal = myDict.get(word, None)
                    newVal = curVal + 1
                    myDict.update({word:newVal})
        d_view = [ (v,k) for k,v in myDict.iteritems() ]
        d_view.sort(reverse=True) # sorts in order of greatest key value and then alphabeticly
        d_view = [ (v,k) for k,v in myDict.iteritems() ]
        d_view.sort(reverse=True)

        print "Bellow is a frequency rank (bigram) for all of the uniqe words in the text file:"
        for v,k in d_view:
            print "%s: %d" % (k,v)

            
#Prints a trigram frequency table            
def trigram():
    myDict = {}
    sent_text= nltk.sent_tokenize('SyzygyNgramTweets.txt')
    with open('SyzygyNgramTweets.txt') as f:
        #print("hi")
        #For sent in nltk.sent_tokenize(f):
        for line in f:
            #line = 
            ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", line).split())
            tokenizer = TweetTokenizer()
            #word_text = nltk.word_tokenize(f)
            sent_text = tokenizer.tokenize(line)
            #sent_text = nltk.word_tokenize(line)
            
            size = len(sent_text) 
            for i in range(0, size-2):
                if i+1 > size:
                    break
                word = sent_text[i] + ", " + sent_text[i+1] + ", " + sent_text[i+2]

            
               #myBigram.append(word)
               # print(myBigram)
                word = word.lower()
                word = word.strip()
                if myDict.has_key(word) == False:
                    myDict.update({word: 1})
                else:
                    curVal = myDict.get(word, None)
                    newVal = curVal + 1
                    myDict.update({word:newVal})
        d_view = [ (v,k) for k,v in myDict.iteritems() ]
        d_view.sort(reverse=True) # sorts in order of greatest key value and then alphabeticly
        d_view = [ (v,k) for k,v in myDict.iteritems() ]
        d_view.sort(reverse=True)

        print "Bellow is a frequency rank (bigram) for all of the uniqe words in the text file:"
        for v,k in d_view:
            print "%s: %d" % (k,v)
         
        
#Adds "s" to beginnin of tweets and "e" to end.
def beginandend():
    prefix = 'S '
    suffix = ' E'

    with open('SyzygyNgramTweets.txt', 'r') as src:
        with open('newSyz.txt', 'w') as dest:
            for line in src:
                line = re.sub('".*?"', '', line)
                ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", line).split())
                
                dest.write('%s%s%s\n' % (prefix, line.rstrip('\n'), suffix))


#Prints sentiment analysis for tweets
#The following code is credited to: http://www.geeksforgeeks.org/twitter-sentiment-analysis-using-python/
def get_tweet_sentiment():
    '''
    Utility function to classify sentiment of passed tweet
    using textblob's sentiment method
    '''
    myDict = {}
    # create TextBlob object of passed tweet text
    nltk.sent_tokenize('SyzTweets.txt')
    with open('SyzTweets.txt') as f:
        #print("hi")
        #For sent in nltk.sent_tokenize(f):
        for line in f:
            analysis = TextBlob(line)
            # set sentiment
            #print score
            score = analysis.sentiment.polarity
            #print score
            if score > 0.0:
                #print ('positive:', analysis.sentiment.polarity, line)
               
                myDict.update({line: score})
            elif score == 0.0:
                #print ('neutral:', analysis.sentiment.polarity, line)
                myDict.update({line: score})
            else:
                #print ('negative', analysis.sentiment.polarity, line)
                myDict.update({line: score})
                
        #print myDict
        sorted_x = sorted(myDict.items(), key=operator.itemgetter(1))
        sorted_x = reversed(sorted_x)
        for v,k in sorted_x:
            print "%s: %s" % (k,v)
        #print type(sorted_x)

        
def main():   
    #word_Tokenize()
    #bigram()
    #trigram()
    get_tweet_sentiment()
if __name__ == '__main__':
    main()



