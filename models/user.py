from enum import Enum
from typing import Optional

from pydantic import BaseModel


class UserType(Enum):
    RegularUser = 1
    AdminUser = 2


class User(BaseModel):
    username: str
    email: str
    password: str
    user_type: Optional[UserType] = None


class AdminUser(User):
    user_type = UserType.AdminUser


class RegularUser(User):
    user_type = UserType.RegularUser
