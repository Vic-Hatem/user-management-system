from pydantic import BaseModel, Field, EmailStr
from user_service import *


class User(BaseModel):
    username: str
    email: str
    password: str


class AdminUser(User):
    def user_type(self):
        return "Admin user type"


class RegularUser(User):
    def user_type(self):
        return "Regular user type"