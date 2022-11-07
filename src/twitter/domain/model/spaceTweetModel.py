from src.shared import ClassToDict


class SpaceTweetModel(ClassToDict):
    id: str
    text: str
    created_at: str
    author_id: str

    __slots__ = ['id', 'text', 'created_at', 'author_id']

    def __init__(self, id: str, text: str, created_at: str, author_id: str):
        self.author_id = author_id
        self.created_at = created_at
        self.text = text
        self.id = id
