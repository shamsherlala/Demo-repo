import tweepy

# Replace these with your own API key, API secret key, Access token, and Access token secret
consumer_key = 'tcS4UzXOu96kghpAdcay9SZdh'
consumer_secret = 'rTYLsAgq6e8Uw2UKE4Qora4VPji87qXM43SzzihvfGY7esvpYg'
access_token = '1695813946341519360-06AqgQvEuK78bHNs8VttChh49DF5Vk'
access_token_secret = '90QMFeDQy87fUZvMnQcQ4Wi7HnJJVWyXZ84qcB81Ib3pl'

# Set up Tweepy with your credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create the API object without specifying the version
api = tweepy.API(auth)

# Specify the username and number of tweets to retrieve
username = 'elonmusk'
num_tweets = 10

# Retrieve tweets using API v2
tweets = api.user_timeline(screen_name=username, count=num_tweets, tweet_mode="extended", lang="en", tweet_type="extended")

# Print the tweets
for tweet in tweets:
    print(tweet.full_text)
    print('-' * 50)
