#######################################################################################################################
# File: image_processing.py
#
#######################################################################################################################
#imports
import cv2
import matplotlib.pyplot as plt
from PIL import Image
file_name = "puzzle_cropped.png"

def process_image_file(file):
    img_to_crop = Image.open(file)
    width, height = img_to_crop.size

    # Setting the points for cropped image
    left = 915
    top = 725
    right = 1300
    bottom = 330
    img_cropped = img_to_crop.crop((left,bottom,right,top))

    img_cropped.save(file_name)
    img_cropped.show()

    img = cv2.imread(file_name)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 6)
    # blur = cv2.bilateralFilter(gray,9,75,75)
    threshold_img = cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 2)
    plt.figure()
    plt.imshow(threshold_img)
    plt.show()
    return img