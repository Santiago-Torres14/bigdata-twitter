import abc

from src.twitter import domain


class GetSpaceInfoByIdRepositoryI(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return hasattr(subclass, 'getSpaceInfoById') and callable(subclass.getSpaceInfoById)

    @abc.abstractmethod
    def getSpaceInfoById(self, id: str, expansions: list[str] or None, user_fields: list[str] or None,
                         space_fields: list[str] = ['host_ids', 'created_at', 'creator_id', 'ended_at', 'lang',
                                                    'is_ticketed', 'participant_count', 'scheduled_start',
                                                    'speaker_ids', 'started_at', 'state', 'topic_ids',
                                                    'title']) -> domain.model.Spaces:
        raise NotImplementedError
