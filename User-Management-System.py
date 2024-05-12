from fastapi import FastAPI,Depends, HTTPException, status
from pydantic import BaseModel,Field,EmailStr
from enum import Enum
from abc import ABC, abstractmethod
from typing import Optional



users= {}


class Type(Enum):
    Admin = 1
    Regular = 2
    Visitor = 3


# Interface
class IUserService(ABC):
    @abstractmethod
    def do_stuff(self):
        pass


# Interface
class IUserCreation(ABC):
    @abstractmethod
    def create(self, user):
        pass


# Interface
class IUserProfileUpdate(ABC):
    @abstractmethod
    def update(self, user):
        pass


# Interface
class IUserRetrieval(ABC):
    @abstractmethod
    def retrieve(self, user):
        pass


class UserCreation(IUserCreation):

    def create(self, user):
        user.append(User(user))
        return None


class UserProfileUpdate(IUserProfileUpdate):

    def update(self, user,new_user):
        if user in users:
            users[users.index(user)] = new_user
            return "updated"
        return "user not exist"


class UserRetrieval(IUserRetrieval):
    def retrieve(self, user):
        if user in users:
            return user


class User(BaseModel):
    username: str
    email: str
    password: str

    def user_type(self):
        return "Generic user type"


class LoginCredentials(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=64)


class AuthenticationService:

    def authenticate_user(self, email: str, password: str):
        if email in users.keys():
            if users[email].passowrd == password:
                return True

        return False


class UserService():


    def add(self,user):
        return UserCreation().create(user)

    def update(self,user,new_user):
        return UserProfileUpdate().update(user,new_user)

    def retrieve(self,user):
        return UserRetrieval().retrieve(user)


'''
class UserService(User):
    
    
    
    user_t: Type

    @staticmethod
    def admin_user():
        print("im in admin")

    @staticmethod
    def regular_user():
        print("im in regular")

'''


class AdminUser(User,UserService):
    def user_type(self):
        return "Admin user type"


class RegularUser(User,UserService):
    def user_type(self):
        return "Regular user type"


app = FastAPI()


def get_authentication_service():
    return AuthenticationService()


@app.post("/login")
def login(credentials: LoginCredentials, auth_service: AuthenticationService = Depends(get_authentication_service)):
    if auth_service.authenticate_user(credentials.email, credentials.password):
        return {"message": "User authenticated successfully!"}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password"
    )


def get_user_service():
    return UserService()


@app.post("/user/")
def add_user(user,user_service: UserService = Depends(get_user_service())):

    return user_service.add(user)


@app.put("/user/{user}")
def update_user( user, new_user, user_service: UserService = Depends(get_user_service())):
    return user_service.update(user, new_user)


@app.get("/user/{user}")
def retrieve_user(user,user_service: UserService = Depends(get_user_service())):
    return user_service.retrieve(user)


def main():

    user_service = UserService(username="test", email="qqqq@gmail.com", password="000", user_t=Type.Regular)
    if user_service.user_t.value == 1:
        user_service.admin_user()
    elif user_service.user_t.value == 2:
        user_service.regular_user()

    admin = AdminUser(username="test",email="qqqq@gmail.com",password="000")
    regular = RegularUser(username="test2", email="3333@gmail.com", password="2222")

    def user_type(user):
        print(user.user_type())

    user_type(admin)
    user_type(regular)


if __name__ == "__main__":
    main()







