from src.twitter import domain
from .twitterApiConnect import twitterClient


class GetSpaceInfoById(domain.repository.GetSpaceInfoByIdRepositoryI):

    def getSpaceInfoById(self, id: str, user_fields: list[str] or None = None,
                         expansions: list[str] or None = ["creator_id"],
                         space_fields: list[str] = ['host_ids', 'created_at', 'creator_id', 'ended_at', 'lang',
                                                    'is_ticketed', 'participant_count', 'scheduled_start',
                                                    'speaker_ids', 'started_at', 'state', 'topic_ids',
                                                    'title']) -> domain.model.Spaces:
        response = twitterClient.get_space(id=id, expansions=expansions, space_fields=space_fields,
                                           user_fields=user_fields)
        includes = response.includes
        data = response.data

        creatorIds = list()
        for creator_id in includes.get('users'):
            creatorIds.append(creator_id.id)

        return domain.model.Spaces(id=data.id, host_ids=data.host_ids, created_at=data.created_at,
                                   creator_id=creatorIds,
                                   ended_at=data.ended_at,
                                   lang=data.lang,
                                   is_ticketed=data.is_ticketed, invited_user_ids=data.invited_user_ids,
                                   participant_count=data.participant_count, scheduled_start=data.scheduled_start,
                                   speaker_ids=data.speaker_ids, started_at=data.started_at,
                                   state=domain.model.SpaceStates.LIVE if data.state == domain.model.SpaceStates.LIVE else domain.model.SpaceStates.SCHEDULED,
                                   topic_ids=data.topic_ids, title=data.title)
