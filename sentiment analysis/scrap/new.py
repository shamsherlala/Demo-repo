import tweepy
import pandas as pd

consumer_key = 'tcS4UzXOu96kghpAdcay9SZdh'
consumer_key_secret = 'rTYLsAgq6e8Uw2UKE4Qora4VPji87qXM43SzzihvfGY7esvpYg'
access_token = '1695813946341519360-06AqgQvEuK78bHNs8VttChh49DF5Vk'
access_token_secret = '90QMFeDQy87fUZvMnQcQ4Wi7HnJJVWyXZ84qcB81Ib3pl'

auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret, access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

search_query = "'Elon Musk' 'fired'-filter:retweets AND -filter:replies AND -filter:links"
no_of_tweets = 100

try:
    tweets = api.search_tweets(q=search_query, lang="en", count=no_of_tweets, tweet_mode ='extended')

    attributes_container = [[tweet.user.name, tweet.created_at, tweet.favorite_count, tweet.source, tweet.full_text] for tweet in tweets]

    columns = ["User", "Date Created", "Number of Likes", "Source of Tweet", "Tweet"]

    tweets_df = pd.DataFrame(attributes_container, columns=columns)

except BaseException as e:
    print('Status Failed On,',str(e))