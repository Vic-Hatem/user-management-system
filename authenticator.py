from user import User, AdminUser, RegularUser, LoginCredentials
from user_service_interface import UserCheck


class AuthenticationService:

    def authenticate_user(self, credentials: LoginCredentials, user: User) -> bool:

        email = credentials.email
        password = credentials.password

        if user is not None:
            if user.password == password and user.email == email:
                return True
        return False


class AdminUserCheck(UserCheck):
    def check_user(self, user: User) -> bool:
        if isinstance(user, AdminUser):
            return True

        return False


class RegularUserCheck(UserCheck):
    def check_user(self, user: User) -> bool:
        if isinstance(user, RegularUser):
            return True
        return False
