import pyautogui
import pygame
from tkinter import messagebox

pygame.init()
pygame.joystick.init()

joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
print(joysticks)

if pygame.joystick.get_count() == 0:
    messagebox.showerror(title="ControlPC",
                         message="There are no controllers found, please check if your controller is connected properly.")
    pygame.quit()
    exit()

joystick = joysticks[0]
joystick.init()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.JOYBUTTONDOWN:
            print(event)
            if joystick.get_button(0):  
                pyautogui.click()

        if event.type == pygame.JOYHATMOTION:
            print(event)
            hat_x, hat_y = joystick.get_hat(0)  
            move_x = 25 * hat_x
            move_y = 25 * -hat_y

            pyautogui.move(move_x, move_y)
