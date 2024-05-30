from models.login_credintials import LoginCredentials
from models.user import User, UserType
from user_management_service.user_check_interface import UserCheck


class AuthenticationService:

    def authenticate_user(self, credentials: LoginCredentials, user: User | None) -> bool:
        email = credentials.email
        password = credentials.password

        return user is not None and user.password == password and user.email == email


class AdminUserCheck(UserCheck):
    def check_user(self, user: User) -> bool:
        return user.user_type == UserType.AdminUser


class RegularUserCheck(UserCheck):
    def check_user(self, user: User) -> bool:
        return user.user_type == UserType.RegularUser
