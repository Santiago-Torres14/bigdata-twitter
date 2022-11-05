import tweepy
from src.shared import metaSingleton
from src.settings import BEARER_TOKEN, ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_SECRET, CONSUMER_KEY


class TwitterApi(metaclass=metaSingleton.MetaSingleton):
    _apiConnection = None

    def connect(self, bearer_token: str, consumer_key: str, consumer_secret: str, access_token: str,
                access_secret: str):
        if self._apiConnection is None:
            self._apiConnection = tweepy.Client(bearer_token=bearer_token, consumer_key=consumer_key,
                                                consumer_secret=consumer_secret, access_token=access_token,
                                                access_token_secret=access_secret)

        return self._apiConnection


twitterClient = TwitterApi().connect(BEARER_TOKEN, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
