import datetime
import hashlib


def getCurrentTime():
    """Get current time in format HH:MM:SS

    Returns:
        str: Time in format HH:MM:SS
    """
    now = datetime.datetime.now()
    return f"{now.hour}:{now.minute}:{now.second}"


def hashText(text: str):
    hasher = hashlib.sha256(text.encode())
    hex_dig = hasher.hexdigest()
    return hex_dig
