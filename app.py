from fastapi import FastAPI, Depends, HTTPException, status
from get_service import get_user_service, get_authentication_service
from authenticator import LoginCredentials, AuthenticationService
from user import User

app = FastAPI()

users = {}

user_service = get_user_service()


@app.post("/login")
def login(credentials: LoginCredentials, auth_service: AuthenticationService = Depends(get_authentication_service)):
    if auth_service.authenticate_user(credentials.email, credentials.password):
        return {"message": "User authenticated successfully!"}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password"
    )


@app.post("/user/{user}")
def add_user(user: User = Depends(get_user_service)):
    if get_authentication_service().AdminUserCheck().check_user(User):
        return user_service.add(user, users)
    return None


@app.put("/user/{user}")
def update_user(user: User = Depends(get_user_service), updated_user: User = Depends(get_user_service)):
    if get_authentication_service().AdminUserCheck().check_user(User):
        return user_service.update(user, updated_user, users)
    return None


@app.get("/user/{user}")
def retrieve_user(user: User = Depends(get_user_service)):
    return user_service.retrieve(user, users)
