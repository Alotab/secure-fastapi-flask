# handling routing operations such as registration and signing-in of users
# The user route will consist of sign-in, sign-out, and sign-up routes

from fastapi import APIRouter, HTTPException, status
from models.user import User, UserSignIn

user_router = APIRouter(
    tags=["User"]
)

# The route checks whether a user with a similar 
# email address exists in the database before adding a new one

users = {}
@user_router.post("/signup")
async def sign_new_user(data: NewUser) -> dict:
    if data.email in users:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with supplied username exists"
        )

    users[data.email] = data
    return {
        "message": "User successfully registered!"
    }


# check whether such a user exists in the database, and if the user doesn’t exist, an exception is raised. 
# If the user exists, the application proceeds to check whether the passwords match before returning a successful message or an exception
@user_router.post("/signin")
async def sign_user_in(user: UserSignIn) -> dict:
    if users[user.email] not in users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
            detail="User does not exist"
        )
    if users[user.email].password != user.password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
            detail="Wrong credentials passed"
        )

    return {"message": "User signed in successfully"}