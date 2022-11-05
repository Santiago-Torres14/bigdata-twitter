import abc

from src.twitter import domain


class GetSpacesByQueryRepositoryI(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return hasattr(subclass, 'getSpacesByQuery') and callable(subclass.getSpacesByQuery)

    @abc.abstractmethod
    def getSpacesByQuery(self, query: str, expansions: list[str] or None = ["creator_id"], max_results: int = 100,
                         state: domain.model.SpaceStates or None = None,
                         user_fields: list[str] or None = None,
                         space_fields: list[str] = ['host_ids', 'created_at', 'creator_id', 'ended_at', 'lang',
                                                    'is_ticketed', 'participant_count', 'scheduled_start',
                                                    'speaker_ids', 'started_at', 'state', 'topic_ids',
                                                    'title']) -> list[domain.model.Spaces]:
        raise NotImplementedError
