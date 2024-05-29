from abc import ABC, abstractmethod

from models.user import User


class UserCheck(ABC):
    @abstractmethod
    def check_user(self, user: User):
        pass
