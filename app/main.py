##############################
#                            #
#  Jacek Jendrzejewski 2022  #
#                            #
##############################

# Imports
import app.Helpers.myMath as myMath
import app.Helpers.myImgProcessing as myImgProcessing
import app.Helpers.myUser as myUser
import app.Helpers.usersDB as usersDB
import app.Helpers.myUtils as myUtils


import io
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends, FastAPI, HTTPException, status

#
app = FastAPI()
users = usersDB.UsersDatabase()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/")
async def root():
    return "Advanced Programming - Jacek Jendrzejewski"


@app.get("/prime/{number}")
async def prime(number: int):
    """Api endpoint that checks if given number is a prime number

    Args:
        number (int): Number

    Returns:
        str: Response whether number is prime or not

    """
    validation = myMath.validateForPrime(number)
    if validation is False:
        return f"Provided number:{number} is invalid."

    isPrime = myMath.isPrime(number)
    primeText = "prime" if isPrime else "not prime"
    return f"Provided number: {number} is {primeText}."


@app.post("/picture/invert2")
async def invert_picture_colors2(file: bytes = File(...)):
    """Inverts colors of given image

    Args:
        file (UploadFile, optional): _description_. Defaults to File(...).

    Returns:
        StreamingResponse: Response with inverted image ready to download
    """
    image = myImgProcessing.invertColors(file)
    newFileName = myImgProcessing.getInvertedFileName("Test.png")

    response = StreamingResponse(io.BytesIO(
        image), media_type='application/octet-stream')
    response.headers["Content-Disposition"] = f"attachment; filename={newFileName}"

    return response


@app.post("/picture/invert")
async def invert_picture_colors(file: UploadFile = File(...)):
    """Inverts colors of given image

    Args:
        file (UploadFile, optional): _description_. Defaults to File(...).

    Returns:
        StreamingResponse: Response with inverted image ready to download
    """
    fileContent = await file.read()
    image = myImgProcessing.invertColors(fileContent)
    newFileName = myImgProcessing.getInvertedFileName(file.filename)

    response = StreamingResponse(io.BytesIO(
        image), media_type='application/octet-stream')
    response.headers["Content-Disposition"] = f"attachment; filename={newFileName}"

    return response


async def get_current_user(token: str = Depends(oauth2_scheme)) -> myUser.DbUser:
    """Tries to get current user from database. Raises error if fails.

    Args:
        token (str, optional): user token, login by default. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: If user is not in database

    Returns:
        myUser.DbUser: user from database
    """
    user = users.getUserByLogin(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User does not exist!",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


async def get_current_active_user(current_user: myUser.DbUser = Depends(get_current_user)) -> myUser.DbUser:
    """Checks if current user is active. If not raises exception.

    Args:
        current_user (myUser.DbUser, optional): Database user. Defaults to Depends(get_current_user).

    Raises:
        HTTPException: Is user active

    Returns:
        myUser.DbUser: Database user.
    """
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@app.post("/token")
async def get_token(form_data: OAuth2PasswordRequestForm = Depends()) -> object:
    """Gets token and its type, based on user crudentials.

    Args:
        form_data (OAuth2PasswordRequestForm, optional): User data. Defaults to Depends().

    Raises:
        HTTPException: User does not exists in database
        HTTPException: Incorrect password

    Returns:
        object: JSON Object with token and its type.
    """
    user = users.getUserByLogin(form_data.username)
    if not user:
        raise HTTPException(
            status_code=400, detail="User does not exist in database")

    hashed_password = myUtils.hashText(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(
            status_code=400, detail="Incorrect password")

    return {"access_token": user.login, "token_type": "bearer"}


@app.get("/user/login")
async def user_login(current_user: myUser.DbUser = Depends(get_current_active_user)):
    """Return current time after successful authorization
    Default user data:
    Login: DefaultUser
    Password: Pass25

    Args:
        current_user (myUser.DbUser, optional): _description_. Defaults to Depends(get_current_active_user).

    Returns:
        str: string message with current time
    """
    return f"Current time is {myUtils.getCurrentTime()}"
