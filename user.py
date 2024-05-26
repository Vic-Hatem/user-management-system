import json

from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    username: str
    email: str
    password: str

    def to_dict(self):
        return {
            'username': self.username,
            'email': self.email,
            'password': self.password,
        }
    def to_json(self):
        return json.dumps(self.to_dict(), indent=3)

class AdminUser(User):
    def user_type(self):
        return "Admin user type"


class RegularUser(User):
    def user_type(self):
        return "Regular user type"
