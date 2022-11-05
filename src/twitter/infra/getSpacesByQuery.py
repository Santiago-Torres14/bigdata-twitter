from .getSpaceInfoById import GetSpaceInfoById
from .twitterApiConnect import twitterClient
from src.twitter import domain


class GetSpacesByQuery(domain.repository.GetSpacesByQueryRepositoryI):

    def getSpacesByQuery(self, query: str, expansions: list[str] or None = None, max_results: int = 100,
                         state: domain.model.SpaceStates or None = None, user_fields: list[str] or None = None,
                         space_fields: list[str] = ['host_ids', 'created_at', 'creator_id', 'ended_at', 'lang',
                                                    'is_ticketed', 'participant_count', 'scheduled_start',
                                                    'speaker_ids', 'started_at', 'state', 'topic_ids',
                                                    'title']) -> list[domain.model.Spaces]:
        response = twitterClient.search_spaces(query=query, max_results=max_results)

        data = response.data
        spaces = list()

        for d in data:
            spaces.append(
                GetSpaceInfoById().getSpaceInfoById(id=d.id, space_fields=space_fields, user_fields=user_fields))

        return spaces
