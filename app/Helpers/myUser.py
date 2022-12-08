from pydantic import BaseModel


class RegisterUser(BaseModel):
    """Simple user class for register api

    Args:
        BaseModel (BaseModel): BaseModel from pydantic
    """
    name: str
    last_name: str
    login: str
    password: str


class LoginUser(BaseModel):
    """Simple user class. Contains only login and password.

    Args:
        BaseModel (BaseModel): BaseModel from pydantic
    """
    login: str
    password: str


class DbUser():
    """Simple user class used in database.
    """

    def __init__(self, id: int, name: str, last_name: str, login: str, hashed_pass: str):
        self.id = id
        self.name = name
        self.last_name = last_name
        self.login = login
        self.hashed_password = hashed_pass
        self.disabled = False
