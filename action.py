from typing import Optional


class Action:

    def __init__(self, id: int, description: Optional[str] = None):

        self.id = id
        self.description = description

    def __repr__(self):
        return f"Action(id: {self.id}, description: {self.description})"

    def __eq__(self, other):
        if not isinstance(other, Action):
            return False
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)
