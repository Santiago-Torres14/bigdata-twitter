from src.twitter import domain
from src.twitter.domain.repository import GetSpacesTweetsByIdRepositoryI
from .twitterApiConnect import twitterClient
from src.twitter.domain.model import SpaceTweetModel


class GetSpaceTweetsById(GetSpacesTweetsByIdRepositoryI):
    def getSpacesTweetsById(self, id: str, expansions: list[str] or None = None, media_fields: list[str] or None = None,
                            place_fields: list[str] or None = None, poll_fields: list[str] or None = None,
                            user_fields: list[str] or None = None,
                            tweet_fields: list[str] = ["author_id", "created_at"]) -> list[domain.model.SpaceTweetModel]:
        response = twitterClient.get_space_tweets(id=id, expansions=expansions, media_fields=media_fields,
                                                  place_fields=place_fields, poll_fields=poll_fields,
                                                  user_fields=user_fields, tweet_fields=tweet_fields)

        data = response.data

        tweets = list()
        for d in data:
            tweets.append(SpaceTweetModel(id=d.id, author_id=d.author_id, text=d.text, created_at=d.created_at))

        return tweets
