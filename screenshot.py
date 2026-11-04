from WinPos import get_window_pos
from PIL import ImageGrab
import win32gui

def takeScreenshot(window):
    hwnd = win32gui.FindWindow(None, window) #finds the window handle for the given window name
    image = ImageGrab.grab(all_screens=True, window=hwnd) #all screen=True so that if it is on a different monitor it will still take the screenshot
    image.save(f'images/screenshot{screenshotCouter()}.png')

def screenshotCouter():
    with open("images/screenshotCounter.txt", "a+") as file:
        file.seek(0)
        if file.read() != "": #reads from the file if there is already a number in the file, if not it will set the counter to 0
            file.seek(0)
            screenshotCount = int(file.read())
        else:
            screenshotCount = 0

        screenshotCount = screenshotCount + 1 
        file.truncate(0) #resets the file and then writes the new number to the file
        file.write(str(screenshotCount))
        return screenshotCount

takeScreenshot('Steins;Gate')

