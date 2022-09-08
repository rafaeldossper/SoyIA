from skimage.transform import resize
from skimage.io import imread,imsave

import cv2

def transformImageToSquareWithPadding(image):
    height, width, channels = image.shape

    if height>width:
        sizeOffset = height-width
        paddingSizeForEachSide = int(sizeOffset/2)
        image = cv2.copyMakeBorder(image, 0, 0,paddingSizeForEachSide, paddingSizeForEachSide, cv2.BORDER_CONSTANT)

    if height<width:
        sizeOffset = width-height
        paddingSizeForEachSide = int(sizeOffset/2)
        image = cv2.copyMakeBorder(image, paddingSizeForEachSide, paddingSizeForEachSide,0, 0, cv2.BORDER_CONSTANT)

    return image


def resizeImageSameSize(image):
    image_downscaled = resize(image, (256, 256,3))
    return image_downscaled

def preProcessing(image):
    image = transformImageToSquareWithPadding(image)
    image = resizeImageSameSize(image)
    return image