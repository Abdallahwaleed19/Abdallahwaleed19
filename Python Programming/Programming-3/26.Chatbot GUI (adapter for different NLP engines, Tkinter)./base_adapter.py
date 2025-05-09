
from abc import ABC, abstractmethod

class NLPAdapter(ABC):
    @abstractmethod
    def get_response(self, user_input: str) -> str:
        pass
