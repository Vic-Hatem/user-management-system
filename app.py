
from fastapi import FastAPI, Depends, HTTPException, status
from user_service import *
from authenticator import *
from __init__ import *

app = FastAPI()

users = {}


def get_user_service():
    return UserService()


def get_authentication_service():
    return AuthenticationService()


user_service=get_user_service()


@app.post("/login")
def login(credentials: LoginCredentials, auth_service: AuthenticationService = Depends(get_authentication_service)):
    if auth_service.authenticate_user(credentials.email, credentials.password):
        return {"message": "User authenticated successfully!"}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password"
    )


@app.post("/user/{user}")
def add_user(user):

    return user_service.add(user, users)


@app.put("/user/{user}")
def update_user(user, updated_user):

    return user_service.update(user, updated_user, users)


@app.get("/user/{user}")
def retrieve_user(user):
    return user_service.retrieve(user, users)