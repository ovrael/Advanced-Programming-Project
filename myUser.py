from pydantic import BaseModel


class RegisterUser(BaseModel):
    name: str
    last_name: str
    login: str
    password: str


class LoginUser(BaseModel):
    login: str
    password: str


class DbUser():
    def __init__(self, id: int, name: str, last_name: str, login: str, hashed_pass: str):
        self.id = id
        self.name = name
        self.last_name = last_name
        self.login = login
        self.hashed_password = hashed_pass
        self.disabled = False
