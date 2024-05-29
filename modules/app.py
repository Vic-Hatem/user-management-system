from fastapi import FastAPI, HTTPException, status

from models.login_credintials import LoginCredentials
from models.user import User
from modules.resources import get_user_service, get_authentication_service

app = FastAPI()


@app.post("/login")
def login(credentials: LoginCredentials, user: User):
    response = get_user_service().retrieve(user)
    if response is not None:

        if get_authentication_service().authenticate_user(credentials, user):
            return {"message": "User authenticated successfully!"}
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )
    raise HTTPException(
        status_code=404,
        detail="User not found"
    )


@app.post("/add_user")
def add_user(user: User):
    response = get_user_service().create(user)
    if response:
        return {"message": "User has been successfully!"}
    raise HTTPException(status_code=422, detail="Cannot add user, user already exist")


@app.put("/update_user")
def update_user(user: User, new_user: User):
    response = get_user_service().update(user, new_user)
    if response:
        return {"message": "Updated successfully"}
    raise HTTPException(status_code=404, detail="User not found")


@app.post("/get_user")
def retrieve_user(user: User):
    response = get_user_service().retrieve(user)
    if response is not None:
        return response
    raise HTTPException(status_code=404, detail="User not found")
