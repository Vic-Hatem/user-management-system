from modules.authenticator import AuthenticationService
from user_management_service.user_management_interface import IUserManagementService
from user_management_service.user_management_service_dict import UserManagementServiceDict


def get_user_service() -> IUserManagementService:
    return UserManagementServiceDict()


def get_authentication_service() -> AuthenticationService:
    return AuthenticationService()


user_service = get_user_service()
auth_service = get_authentication_service()
