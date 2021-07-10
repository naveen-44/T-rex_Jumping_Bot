from numpy import *
import pyautogui as pyg
import keyboard as kb
from PIL import ImageGrab
from PIL import ImageOps
from time import *

# co-ordinates might change based on how you position the window
replayButton = (960, 548)           # position of the replay button on screen
dino = (665, 571)                   # position of the dino in game on screen


def restartGame():
    # click the restart/replay button
    pyg.click(replayButton)


def image_grab():
    # check a small box in front of the dino if there is tree coming
    box = (dino[0]+55, dino[1], dino[0]+145, dino[1]+5)
    image = ImageGrab.grab(box)
    gray_image = ImageOps.grayscale(image)
    color_box = array(gray_image.getcolors())
    return color_box.sum()          # returning sum of the pixel values in the box


def pressSpace():
    # key down the space for 0.1 second and then key up
    pyg.keyDown('space')
    sleep(0.1)
    pyg.keyUp('space')


sleep(4)
restartGame()

while not kb.is_pressed('q'):       # To stop the bot manually, press 'q'
    if image_grab() != 697:         # value if there is no tree
        pressSpace()
