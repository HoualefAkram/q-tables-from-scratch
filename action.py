from typing import Optional


class Action:

    def __init__(self, id: int):

        def __get_description():
            match id:
                case 0:
                    return "Left"
                case 1:
                    return "Down"
                case 2:
                    return "Right"
                case 3:
                    return "Up"

        self.id = id
        self.description = __get_description()

    def __repr__(self):
        return f"Action(id: {self.id}, description: {self.description})"

    def __eq__(self, other):
        if not isinstance(other, Action):
            return False
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)
