from abc import ABC, abstractmethod

from models.user import User


class IUserManagementService(ABC):
    @abstractmethod
    def create(self, user: User):
        pass

    @abstractmethod
    def update(self, user: User, new_user: User):
        pass

    @abstractmethod
    def retrieve(self, user: User):
        pass

    @abstractmethod
    def check_if_user_exists(self, user: User):
        pass
