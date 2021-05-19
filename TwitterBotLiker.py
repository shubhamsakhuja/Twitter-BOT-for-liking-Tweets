import tweepy
import time

consumer_key = 'xxxxxxxxxxxxxxxxxxxxxxxxx' #<---------------------------------------Actual length
consumer_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' #<-----------Actual length

key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' #<-----------------------Actual length
secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' #<-------------------------Actual length

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

user = api.me()

FILE_NAME = 'last_seen.txt'

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

# The Twitter user who we want to get tweets from
name = "EnterTweetID" #<--------------------------------------------Enter the "@username" of the person
# Number of tweets to pull
tweetCount = 200 #--------------------------------------------------How many tweets you want to like?


# Calling the user_timeline function with our parameters
results = api.user_timeline(id=name, count=tweetCount)

# foreach through all tweets pulled
for tweet in results:
   # printing the text stored inside the tweet object
   #print(tweet.text)
   print(tweet.id)

def reply():
    results = api.user_timeline(id=name, count=tweetCount)
    for tweet in results:
        #print(tweet.text)
        print(tweet.id)
        var = tweet.id
        print(var)
        #api.update_status(status="Auto replied", in_reply_to_status_id=tweet.id,auto_populate_reply_metadata=True)
        api.create_favorite(tweet.id)
        print("liked")
        #api.retweet(tweet.id)      /* UNCOMMENT THE SECTION TO PRINT */
        #print("retweeted")
        #store_last_seen(FILE_NAME, tweet.id)
        #print("stored last tweet id in last_seen.txt "+str(tweet.id))

reply()
