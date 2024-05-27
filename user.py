import json

from pydantic import BaseModel, EmailStr, Field


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


class LoginCredentials(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=64)
