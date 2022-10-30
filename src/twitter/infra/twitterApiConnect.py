import tweepy
from src.shared import metaSingleton
from src.settings import BEARER_TOKEN, ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_SECRET, CONSUMER_KEY


class TwitterApi(metaclass=metaSingleton.MetaSingleton):
    _apiConnection = None

    def connect(self, BEARER_TOKEN: str, CONSUMER_KEY: str, CONSUMER_SECRET: str, ACCESS_TOKEN: str,
                ACCESS_SECRET: str):
        if self._apiConnection is None:
            self._apiConnection = tweepy.Client(bearer_token=BEARER_TOKEN, consumer_key=CONSUMER_KEY,
                                                consumer_secret=CONSUMER_SECRET, access_token=ACCESS_TOKEN,
                                                access_token_secret=ACCESS_SECRET)

        return self._apiConnection


twitterClient = TwitterApi().connect(BEARER_TOKEN, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
