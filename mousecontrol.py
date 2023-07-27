import pyautogui
import random

def func():
    width = random.randint(1,1920)
    height = random.randint(1,1080)
    pyautogui.moveTo(width,height, duration=0)