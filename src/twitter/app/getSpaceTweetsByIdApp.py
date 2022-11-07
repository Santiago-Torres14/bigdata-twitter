from src.shared import databaseConnection
from src.twitter import infra

class GetSpaceTweetsByIdApp:
    def getSpaceTweetsById(id: str) -> list:
        tweetsCollection = databaseConnection['tweets']
        tweets = infra.GetSpaceTweetsById().getSpacesTweetsById(id=id)

        tweetsDict = list()
        for tweet in tweets:
            tweetDict = tweet.slotted_to_dict()
            tweetDict.update(space_id=id)
            tweetsDict.append(tweetDict)

        return tweetsCollection.insert_many(tweetsDict).inserted_ids

