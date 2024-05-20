from user_interface import *
from user import *


class UserCreation(IUserCreation):

    def create(self, user, users):
        if users[user.email]:
            '''user already exists'''
            return False

        else:
            users[user.email]=user
            return True


class UserProfileUpdate(IUserProfileUpdate):

    def update(self, user, new_user, users):
        if not users[user.email]:
            '''
            user doesn't exist!
            should we add a new user if the we want to update a user that doesnt exist?!
            '''
            return False
        else:
            users[user.email] = new_user
            return True


class UserRetrieval(IUserRetrieval):

    def retrieve(self, user, users):
        if users[user.email]:
            return users[user.email]

        '''user doesnt exist'''
        return None


class UserService:

    def add(self,user, users):
        return UserCreation().create(user, users)

    def update(self,user,new_user, users):
        return UserProfileUpdate().update(user,new_user, users)

    def retrieve(self,user, users):
        return UserRetrieval().retrieve(user, users)
