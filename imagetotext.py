import os
import pytesseract
from PIL import Image
import sys

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"                        #Path of tesseract

def convert():
    img = Image.open('testimg.jpg')
    text = pytesseract.image_to_string(img)
    print(text)

convert()