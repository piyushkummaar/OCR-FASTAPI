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

class IMAGETOTEXT:
    def __init__(self):
        '''
        repr : Initializing the tesseract path
        '''
        
        if sys.platform == 'win32':
            pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
        else:
            pytesseract.pytesseract.tesseract_cmd = r"usr/bin/tesseract"
    def dodgeV2(self,x,y):
        return cv2.divide(x,255-y,scale=256)
        

    def extracttext(self,image):
        img = cv2.imread(image)
        img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        img_invert = cv2.bitwise_not(img_gray) #gray scale to inversion of the image
        lines = pytesseract.image_to_string(img_invert, lang='eng')
        lines = lines.split("\n")
        count = 1
        extract = dict()
        
        for text in lines:
            if len(text) > 0 or text != "  ":
                extract[f"line {count}"] = text
            count += 1
        return extract 
