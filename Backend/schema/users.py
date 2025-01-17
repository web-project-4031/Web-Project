from pydantic import BaseModel


class UserSignIn(BaseModel):
    user_name: str
    password: str
    role: bool
    