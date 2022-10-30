

class SpaceTweetModel:
    id: str
    text: str
    created_at: str
    author_id: str
    conversation_id: str
    
    def __init__(self, id: str, text: str, created_at: str, author_id: str, conversation_id: str):
        self.conversation_id = conversation_id
        self.author_id = author_id
        self.created_at = created_at
        self.text = text
        self.id = id
        
