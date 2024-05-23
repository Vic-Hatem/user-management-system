from abc import ABC

from pydantic import BaseModel, EmailStr, Field
from user import User, AdminUser, RegularUser


class UserCheck(ABC):
    def check_user(self, user: User):
        pass


class LoginCredentials(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=64)


class AuthenticationService:
    @staticmethod
    def authenticate_user(self, email: str, password: str, users: dict[str, User]):
        if email in users:
            if users[email].passowrd == password:
                return True

        return False

    class AdminUserCheck(UserCheck):
        def check_user(self, user: User):
            if isinstance(user, AdminUser):
                return True

            return False

    class RegularUserCheck(UserCheck):
        def check_user(self, user: User):
            if isinstance(user, RegularUser):
                return True
            return False
