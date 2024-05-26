from fastapi import FastAPI, Depends, HTTPException, status
from get_service import get_user_service, get_authentication_service
from authenticator import LoginCredentials, AuthenticationService
from user import User

app = FastAPI()

users = {"hatem@gmail.com": {"username": "hatem", "email": "hatem@gmail.com", "password": "000000000"}}

user_service = get_user_service()

auth_service = get_authentication_service()


@app.post("/login")
def login(credentials: LoginCredentials):
    print(credentials, type(credentials))
    if auth_service.authenticate_user(credentials.email, credentials.password, users):
        return {"message": "User authenticated successfully!"}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password"
    )


@app.post("/add_user")
def add_user(user:User):
    if user_service.add(user, users):
        return {"message": "User has been successfully!"}
    raise HTTPException(status_code=422, detail="Cannot add user, user already exist")


@app.put("/update_user/{user}")
def update_user(user, updated_user):
    if user_service.update(user, updated_user, users):
        return {"message": "Updated uccessfully"}
    raise HTTPException(status_code=404, detail="User not found")


@app.get("/get_user")
def retrieve_user(user_email):
    response = user_service.retrieve(user_email, users)
    if response is not None:
        return response
    raise HTTPException(status_code=404, detail="User not found")

