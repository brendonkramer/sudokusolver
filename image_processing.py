#######################################################################################################################
# File: image_processing.py
#
#######################################################################################################################
#imports
import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import pytesseract

file_name = "puzzle_cropped.png"

def crop(file, size_and_loc):
    img_to_crop = Image.open(file)
    width, height = img_to_crop.size
    puzzle_size = size_and_loc[0]
    puzzle_loc = size_and_loc[1]
    # Setting the points for cropped image
    left = puzzle_loc['x']
    top = puzzle_loc['y'] + puzzle_size['height']
    right = puzzle_loc['x'] + puzzle_size['width']
    bottom = puzzle_loc['y']
    img_cropped = img_to_crop.crop((left, bottom, right, top))

    img_cropped.save(file_name)
    #img_cropped.show()
    return file_name

def preprocess(file):
    img = cv2.imread(file)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 1)
    resized_transformed = cv2.resize(blur, (450, 450))
    return resized_transformed

def create_grid(img):
    rows = np.vsplit(img, 9)
    boxes = []
    for r in rows:
        cols = np.hsplit(r, 9)
        for box in cols:
            box_shortened = box[5:45, 5:45]
            boxes.append(box_shortened)
    return boxes

def convert_to_int(img_arr):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    arr = []
    for img in img_arr:
        # plt.figure()
        # plt.imshow(img)
        # plt.show()
        num = pytesseract.image_to_string(img, lang='eng', config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
        #print(num)
        arr.append(num)
    print(arr)
    return arr

def clean_up_puzzle(puzzle_to_clean):
    index_row = 0
    index_col = 0
    puzzle = np.empty([9, 9])
    for cell in puzzle_to_clean:
        print(cell)
        if "\n\f" in cell:
            cell = int(cell[:1])
        elif "\f" in cell:
            cell = 0
        else:
            print("something bad happened")
        puzzle[index_row][index_col] = cell
        index_col += 1
        if index_col >= 9:
            index_row += 1
            index_col = 0
    return puzzle

def process_image_file(file, size_and_loc):
    new_file = crop(file, size_and_loc)
    img = preprocess(new_file)
    img_arr = create_grid(img)
    int_puzzle_unmapped = convert_to_int(img_arr)
    final_puzzle = clean_up_puzzle(int_puzzle_unmapped)
    print(final_puzzle)
    return final_puzzle