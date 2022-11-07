import abc

from src.twitter import domain


class GetSpacesTweetsByIdRepositoryI(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return hasattr(subclass, 'getSpacesTweetsById') and callable(subclass.getSpacesTweetsById)

    @abc.abstractmethod
    def getSpacesTweetsById(self, id: str, expansions: list[str] or None = None, media_fields: list[str] or None = None,
                            place_fields: list[str] or None = None,
                            poll_fields: list[str] or None = None, user_fields: list[str] or None = None,
                            tweet_fields: list[str] = ["author_id", "created_at"]) -> list[domain.model.SpaceTweetModel]:
        raise NotImplementedError
