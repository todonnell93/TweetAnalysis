import tweepy

#create a txt file
f = open("tweetlog.txt","w+")

#define twitter tokens (private)
auth = tweepy.OAuthHandler('nAhbnjpPE6YvQaZnUlkc51elD', 'JH6Dqr06ue25lx3TmUXUtp9WcbEdDFisBzzuCdSunoO6RnPtqT')
auth.set_access_token('35162714-aac3MZ0JcKvciP1YQXvF2ZIANoAAh7UmHwlY42wbG', 'ucquqsErqR6sm5ZQ27URwIQi4HwUWoe54bkd97DOVQIrS')

#define tweepy object
api = tweepy.API(auth)

#pulls 15 of the most recent tweets from my twitter feed
tweet = api.home_timeline(1)

#prints tweet to console
print(dir(tweet))

##https://stackoverflow.com/questions/7714282/return-actual-tweets-in-tweepy
