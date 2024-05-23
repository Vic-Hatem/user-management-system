from user_service import UserService
from authenticator import AuthenticationService


def get_user_service():
    return UserService()


def get_authentication_service():
    return AuthenticationService()
