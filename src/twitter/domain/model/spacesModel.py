from .spaceStatesModel import SpaceStates


class Spaces:
    id: str
    host_ids: list
    created_at: str
    creator_id: str
    ended_at: str or None
    lang: str
    is_ticked: bool
    invited_user_ids: list
    participant_count: int
    scheduled_start: str or None
    speaker_ids: list
    started_at: str or None
    state: SpaceStates
    topic_ids: str or None
    title: str

    def __init__(self, id: str, host_ids: list, created_at: str, creator_id: str, lang: str,
                 is_ticked: bool, invited_user_ids: list, participant_count: int,
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
        self.is_ticked = is_ticked
        self.lang = lang
        self.ended_at = ended_at
        self.creator_id = creator_id
        self.created_at = created_at
        self.host_ids = host_ids
        self.id = id
