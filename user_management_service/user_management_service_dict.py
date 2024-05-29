from models.user import User
from user_management_service.user_management_interface import IUserManagementService


def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class UserManagementServiceDict(IUserManagementService):
    users: dict[str, User]

    def __init__(self):
        self.users = {}

    def check_if_user_exists(self, user: User) -> bool:

        if user.email in self.users:
            return True
        return False

    def create(self, user: User) -> bool:
        if not self.check_if_user_exists(user):
            self.users[user.email] = user

            return True
        return False

    def update(self, user: User, new_user: User) -> bool:
        if self.check_if_user_exists(user):
            self.users[user.email] = new_user
            self.users[new_user.email] = self.users.pop(user.email)
            return True

        return False

    def retrieve(self, user: User) -> User | None:
        if self.check_if_user_exists(user):
            return self.users[user.email]
        return None
