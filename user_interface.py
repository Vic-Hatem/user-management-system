from abc import ABC, abstractmethod
from user import User


# Interface
class IUserCreation(ABC):
    @abstractmethod
    def create(self, user: User, users):
        pass


# Interface
class IUserProfileUpdate(ABC):
    @abstractmethod
    def update(self, user: User, new_user: User, users):
        pass


# Interface
class IUserRetrieval(ABC):
    @abstractmethod
    def retrieve(self, user: User, users):
        pass
