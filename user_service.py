from user_interface import IUserRetrieval, IUserCreation, IUserProfileUpdate
from user import User


class UserCreation(IUserCreation):

    def create(self, user: User, users):
        if user.email in users:
            # user already exists
            return False

        else:
            users[user.email] = user
            return True


class UserProfileUpdate(IUserProfileUpdate):

    def update(self, user: User, new_user: User, users):
        if user.email not in users:
            # user doesn't exist!
            # should we add a new user if the we want to update a user that doesnt exist?!
            return False
        else:
            users[user.email] = new_user
            return True


class UserRetrieval(IUserRetrieval):

    def retrieve(self, user: User, users):
        if user.email in users:
            return users[user.email]

        # user doesnt exist
        return None


class UserService:

    @staticmethod
    def add(self, user: User, users):
        return UserCreation().create(user, users)

    @staticmethod
    def update(self, user: User, new_user: User, users):
        return UserProfileUpdate().update(user, new_user, users)

    @staticmethod
    def retrieve(self, user: User, users):
        return UserRetrieval().retrieve(user, users)
