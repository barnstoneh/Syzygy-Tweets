# Syzygy-Tweets

Execution instructions:

Download all .txt files and .py files to one place. Run Tweepy.py. Tweepy.py is set up right now so that when you run it, all the data will be printed out. To only receive specific data, go to main and comment out every function you do not wish to run. Your options for individual functions are: 
word_Tokenize() – Prints Unigram Frequency chart,
bigram() – Prints Bigram Frequency chart,
trigram() – Prints Trigram Frequency chart and 
get_tweet_sentiment() – Prints tweets in order of their assigned sentiment value

Document Descriptions:

NLPFinalProject – Includes project and ethical statement.
NLPData – Includes majority of data collected from tweets.

CSV/Text File Description:

SyzygyUltimate_tweets.csv – Contains all tweets, including the time they were tweeted and the tweet’s id.
SyzTweets.txt – Used to make the unigram frequency chart and sentiment analyses. Has one tweet per line.
SyzygyNgramTweets.txt – Used to make the bigram and trigram frequency chart. Contains same thing as SyzTweets.txt but, has s at the beginning of each tweet and e at the end of each tweet.
newSyz.txt – Not really used for much, just needed this extra file for one of the functions to write to (just a one time thing).

Libraries Used:

tweepy, csv, nltk, re, TextBlob, decimal, operator, json

