import os
import ctypes
import random

def Wallpaper():
    img = r"C:\Users\saisa\OneDrive\Desktop\Wallpapers"
    list_img = os.listdir(img)
    imgChoice = random.choice(list_img)
    randomImg = os.path.join(img, imgChoice)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, randomImg, 0)
    response = "Background changed successfully"
    return response