from pydantic import BaseModel


class UserSignIn(BaseModel):
    user_name: str
    password: str
    role: bool = False


class UserLogIn(BaseModel):
    user_name: str
    password: str