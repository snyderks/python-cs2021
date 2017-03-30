"""API loads the tweepy authorization for the app."""
import tweepy
from twitterKeys import getKeys

def getAPI():
    """Load an instance of tweepy for use."""
    access_token, access_secret, consumer_key, consumer_secret = getKeys()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)

    return api
