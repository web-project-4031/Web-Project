# section for import libraries
from fastapi import FastAPI

# section for import user defined
from schema.users import UserSignIn, UserLogIn
from database import *
from response import *



app = FastAPI()

@app.get('/')
async def root():
    return{
        "message": "Hello World!"
    }


@app.post('/signin')
async def signin(user: UserSignIn):
    result = check_exist_user(user.user_name)
    if result:
        return UserExist

    values = (
        user.user_name,
        user.password,
        int(user.role)
    )
    
    result = insert_user(values=values)
    if result:
        return OK
    return UnExpected


@app.post('/login')
async def login(user: UserLogIn):
    result = check_exist_user(user_name=user.user_name)
    if not result:
        return UserNotExist
    result = user_password_checker(user.user_name, user.password)
    if result:
        return OK
    return WrongPassword