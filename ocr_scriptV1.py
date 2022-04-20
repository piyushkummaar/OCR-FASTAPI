"""
Created on March 2022
@author: PIYUSH KUMAR
@github: https://github.com/piyushkummaar
"""
import pytesseract
from PIL import Image
import cv2
import numpy as np
import sys
import re

class IMAGETOTEXT:
    def __init__(self):
        '''
        repr : Initializing the tesseract path
        '''
        
        if sys.platform == 'win32':
            pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
        else:
            pytesseract.pytesseract.tesseract_cmd = r"usr/bin/tesseract"

    def extracttext(self,image):
        img = cv2.imread(image)
        img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        img_invert = cv2.bitwise_not(img_gray) #gray scale to inversion of the image

        ######################
        # Binarized image
        th, img_th = cv2.threshold(img_invert, 128, 255, cv2.THRESH_BINARY)

        kernel = np.ones((5,5), np.uint8)       
        # The first parameter is the original image,
        # kernel is the matrix with which image is
        # convolved and third parameter is the number
        # of iterations, which will determine how much
        # you want to erode/dilate a given image.
        # img_erosion = cv2.erode(img_th, kernel, iterations=1)
        img_dilation = cv2.dilate(img_invert, kernel, iterations=1)

        lines = pytesseract.image_to_string(img_dilation, lang='eng')
        lines = lines.split("\n")
        lines = list(filter(None, lines))
        count = 1
        extract = dict()
        
        for text in lines:
            if len(text) > 0 or text !="  ":
                extract[f"line {count}"] = text
            count += 1
        return extract 


# main = IMAGETOTEXT()
# print(main.extracttext('Sample-images/image_picker_2F5070F1-A609-4DAD-B378-F1216DD6B2BE-12309-000005D9E4121B16.jpg'))