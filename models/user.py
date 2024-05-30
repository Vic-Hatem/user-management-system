from abc import abstractmethod
from enum import Enum

from pydantic import BaseModel


class UserType(Enum):
    RegularUser = 1
    AdminUser = 2


class User(BaseModel):
    username: str
    email: str
    password: str

    @property
    @abstractmethod
    def user_type(self) -> UserType:
        pass


class AdminUser(User):
    @property
    def user_type(self) -> UserType:
        return UserType.AdminUser


class RegularUser(User):
    @property
    def user_type(self) -> UserType:
        return UserType.RegularUser
