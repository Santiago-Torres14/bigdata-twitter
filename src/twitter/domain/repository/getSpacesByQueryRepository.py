import abc

from src.twitter import domain


class GetSpacesByQueryRepositoryI(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return hasattr(subclass, 'getSpacesByQuery') and callable(subclass.getSpacesByQuery)

    @abc.abstractmethod
    def getSpacesByQuery(self, query: str, expansions: list[str] or None, max_results: int,
                         state: domain.model.SpaceStates or None,
                         user_fields: list[str] or None,
                         space_fields: list[str]) -> list[domain.model.Spaces]:
        raise NotImplementedError
