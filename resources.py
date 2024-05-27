from authenticator import AuthenticationService
from user_service_interface import IUserManagementService
from user_management_service_dict import UserManagementServiceDict


def get_user_service() -> IUserManagementService:
    return UserManagementServiceDict()


def get_authentication_service() -> AuthenticationService:
    return AuthenticationService()
