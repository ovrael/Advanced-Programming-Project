import cv2
import numpy as np


def invertColors(fileContent):
    """Inverts colors of given image

    Args:
        fileContent: Content from fastapi image file

    Returns:
        Any: cv2 encoded image
    """
    contentArray = np.fromstring(fileContent, np.uint8)  # type: ignore

    image = cv2.imdecode(contentArray, cv2.IMREAD_COLOR)
    rgbImage = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    invertedImage = cv2.bitwise_not(rgbImage)

    _, encodedImage = cv2.imencode('.PNG', invertedImage)

    return encodedImage


def getInvertedFileName(fileName: str) -> str:
    """Creates name for inverted image based on its name

    Args:
        fileName (str): Name of image file

    Returns:
        str: Inverted image file name
    """
    fileNameParts = fileName.split('.')
    return '.'.join(fileNameParts[:-1]) + "_Inverted." + fileNameParts[-1]
