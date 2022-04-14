"""
Created on March 2022
@author: PIYUSH KUMAR
@github: https://github.com/piyushkummaar
"""
import pytesseract
from PIL import Image
import os
import cv2
import json
import numpy as np
import glob

class IMAGETOTEXT:
    def __init__(self):
        '''
        repr : Initializing the tesseract path
        '''
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

    def dodgeV2(self,x,y):
        return cv2.divide(x,255-y,scale=256)
        

    def extracttext(self,image):
        img = cv2.imread(image)
        img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        img_invert = cv2.bitwise_not(img_gray) #gray scale to inversion of the image
        cv2.imwrite("final_image1.png",img_invert)
        # cv2.imshow("show",img_gray)
        # cv2.waitKey(0) #waits until the pressing any key.
        # cv2.destroyAllWindows() # this function destroy all windows of images after clicking any button.

        # get text from the image        
        lines = pytesseract.image_to_string(img_invert, lang='eng')
        lines = lines.split("\n")
        count = 1
        extract = dict()
        
        for text in lines:
            if len(text) > 0 or text != "  ":
                # print(f"line {count} : {text}")
                extract[f"line {count}"] = text
            count += 1

        # json_obj = json.dumps(extract,indent=4)

        # with open("example.json", "w") as outfile:
        #     outfile.write(json_obj)
        # raw = [lines]
        return extract 

# if __name__ == "__main__":
#     try:
#         im = IMAGETOTEXT()
#         # images = glob.glob('sample-images/*.jpg')
#         # print(images)
#         # for img in images:
#             # break
        
#         # im.extracttext('sample-images\\image_picker_2862CAC0-3608-4D0A-8DBA-62751FF076E0-12309-000005DA9DC00E6A.jpg')
#         im.extracttext('sample-images\\image_picker_2B35241A-66E4-4B7A-A136-2807FFF5E0E3-12309-000005D95A1955B8.jpg')

                    
#     except Exception as e:
#         print(e)