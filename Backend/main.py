# section for import libraries
from fastapi import FastAPI

# section for import user defined
from schema.users import UserSignIn
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
    result = check_exist(user.user_name)
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

