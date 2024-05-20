from abc import ABC, abstractmethod


# Interface
class IUserService(ABC):
    @abstractmethod
    def do_stuff(self):
        pass


# Interface
class IUserCreation(ABC):
    @abstractmethod
    def create(self, user, users):
        pass


# Interface
class IUserProfileUpdate(ABC):
    @abstractmethod
    def update(self, user, new_user, users):
        pass


# Interface
class IUserRetrieval(ABC):
    @abstractmethod
    def retrieve(self, user, users):
        pass
