from fastapi import FastAPI, HTTPException, status

from models.login_credintials import LoginCredentials
from models.user import User
from modules.resources import user_service, auth_service

app = FastAPI()


@app.post("/login")
def login(credentials: LoginCredentials, user: User):
    response = user_service.get(user)
    if response is not None:

        if auth_service.authenticate_user(credentials, user):
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
    response = user_service.create(user)
    if response:
        return {"message": "User has been successfully!"}
    raise HTTPException(status_code=422, detail="Cannot add user, user already exist")


@app.put("/update_user")
def update_user(user: User, new_user: User):
    response = user_service.update(user, new_user)
    if response:
        return {"message": "Updated successfully"}
    raise HTTPException(status_code=404, detail="User not found")


@app.post("/get_user")
def get_user(user: User):
    response = user_service.get(user)
    if response is not None:
        return response
    raise HTTPException(status_code=404, detail="User not found")
