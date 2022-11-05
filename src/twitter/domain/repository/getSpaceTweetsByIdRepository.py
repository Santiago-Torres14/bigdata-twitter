import abc

from src.twitter import domain


class GetSpacesTweetsByIdRepositoryI(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return hasattr(subclass, 'getSpacesTweetsById') and callable(subclass.getSpacesTweetsById)

    @abc.abstractmethod
    def getSpacesTweetsById(self) -> list[domain.model.SpaceTweetModel]:
        raise NotImplementedError