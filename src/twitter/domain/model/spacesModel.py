from .spaceStatesModel import SpaceStates


class Spaces:
    id: str
    host_ids: list
    created_at: str
    creator_id: list[str]
    ended_at: str or None
    lang: str
    is_ticketed: bool
    invited_user_ids: list
    participant_count: int
    scheduled_start: str or None
    speaker_ids: list
    started_at: str or None
    state: SpaceStates
    topic_ids: str or None
    title: str

    __slots__ = ['id', 'host_ids', 'created_at', 'creator_id', 'lang', 'is_ticketed', 'invited_user_ids',
                 'participant_count', 'scheduled_start', 'speaker_ids', 'started_at', 'state', 'topic_ids', 'title',
                 'ended_at']

    def __init__(self, id: str, host_ids: list, created_at: str, creator_id: list[str], lang: str,
                 is_ticketed: bool, invited_user_ids: list, participant_count: int,
                 speaker_ids: list, state: SpaceStates, title: str, ended_at: str or None = None,
                 started_at: str or None = None, scheduled_start: str or None = None,
                 topic_ids: str or None = None) -> None:
        self.title = title
        self.topic_ids = topic_ids
        self.state = state
        self.started_at = started_at
        self.speaker_ids = speaker_ids
        self.scheduled_start = scheduled_start
        self.participant_count = participant_count
        self.invited_user_ids = invited_user_ids
        self.is_ticketed = is_ticketed
        self.lang = lang
        self.ended_at = ended_at
        self.creator_id = creator_id
        self.created_at = created_at
        self.host_ids = host_ids
        self.id = id

    def slotted_to_dict(self):
        return {s: getattr(self, s) for s in self.__slots__ if hasattr(self, s)}

    # def __repr__(self) -> str:
    #     # TODO
    #     # return the id and name of the space
    #     pass
