import datetime
import hashlib


def getCurrentTime() -> str:
    """Get current time in format HH:MM:SS

    Returns:
        str: Time in format HH:MM:SS
    """
    now = datetime.datetime.now()
    return f"{now.hour}:{now.minute}:{now.second}"


def hashText(text: str) -> str:
    """Hashes text using sha256 algorithm from hashlib package

    Args:
        text (str): Text

    Returns:
        str: Hashed text in hexdigest
    """
    hasher = hashlib.sha256(text.encode())
    hex_dig = hasher.hexdigest()
    return hex_dig
