
from pydantic import BaseModel, EmailStr, Field
from user import *


class LoginCredentials(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=64)


class AuthenticationService:
    @staticmethod
    def authenticate_user(self, email: str, password: str, users: dict[str,User]):
        if email in users.keys():
            if users[email].passowrd == password:
                return True

    @staticmethod
    def authority_check(self,user: User):

        if isinstance(user,AdminUser):
            return True

        return False
