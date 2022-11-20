from .myUser import *
from .myUtils import *


class UsersDatabase:
    def __init__(self):
        self.users = []
        self.addDefaultUser()

    def addDefaultUser(self):
        id = 0 if len(self.users) == 0 else self.users[-1].id + 1
        dbUser = DbUser(
            id,
            "DefaultName",
            "DefaultLastName",
            "DefaultUser",
            hashText("Pass25")
        )

        if (dbUser not in self.users):
            self.users.append(dbUser)
            return True
        else:
            return False

    def addUser(self, user: RegisterUser):
        id = 0 if len(self.users) == 0 else self.users[-1].id + 1
        dbUser = DbUser(
            id,
            user.name,
            user.last_name,
            user.login,
            hashText(user.password)
        )

        if (dbUser not in self.users):
            self.users.append(dbUser)
            return True
        else:
            return False

    def removeUser(self, user: DbUser):
        if (user in self.users):
            self.users.remove(user)
            return True
        else:
            return False

    def getUserByLogin(self, login: str):
        for user in self.users:
            if user.login == login:
                return user

        return None
