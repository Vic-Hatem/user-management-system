import json

from user_interface import IUserRetrieval, IUserCreation, IUserProfileUpdate
from user import User


class UserCreation(IUserCreation):

    def create(self, user: User, users):

        user = json.loads(user)
        if user["email"] in users:
            # user already exists
            return False

        else:
            users[user["email"]] = user
            return True


class UserProfileUpdate(IUserProfileUpdate):

    def update(self, user: User, new_user: User, users):
        user = json.loads(user)
        new_user = json.loads(new_user)
        if user["email"] not in users:
            # user doesn't exist!
            # should we add a new user if the we want to update a user that doesnt exist?!
            return False
        else:
            users[user["email"]] = new_user
            users[new_user["email"]] = users.pop(user["email"])
            return True


class UserRetrieval(IUserRetrieval):

    def retrieve(self, user_email, users):
        if user_email in users:
            return users[user_email]

        # user doesnt exist
        return None


class UserService:

    def add(self, user: User, users):
        return UserCreation().create(user, users)

    def update(self, user: User, new_user: User, users):
        return UserProfileUpdate().update(user, new_user, users)

    def retrieve(self, user_email, users):
        return UserRetrieval().retrieve(user_email, users)
