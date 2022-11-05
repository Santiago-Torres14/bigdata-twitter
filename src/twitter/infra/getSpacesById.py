from src.twitter import domain
from .getSpaceInfoById import GetSpaceInfoById
from .twitterApiConnect import twitterClient


class GetSpacesById(domain.repository.GetSpacesByIdRepositoryI):

    def getSpacesById(self, id: list[str], expansions: list[str] or None = None, user_fields: list[str] or None = None,
                      space_fields: list[str] = ['host_ids', 'created_at', 'creator_id', 'ended_at', 'lang',
                                                 'is_ticketed', 'participant_count', 'scheduled_start',
                                                 'speaker_ids', 'started_at', 'state', 'topic_ids',
                                                 'title']) -> list[domain.model.Spaces]:
        response = twitterClient.get_spaces(ids=id)

        data = response.data
        spaces = list()

        for d in data:
            spaces.append(
                GetSpaceInfoById().getSpaceInfoById(id=d.id, space_fields=space_fields, user_fields=user_fields))

        return spaces
