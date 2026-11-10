from PIL import ImageGrab
import win32gui
import files

def takeScreenshot(window):
    hwnd = win32gui.FindWindow(None, window) #finds the window handle for the given window name
    image = ImageGrab.grab(all_screens=True, window=hwnd) #all screen=True so that if it is on a different monitor it will still take the screenshot
    screenShotNum = files.fileCouter("images/screenshotCounter.txt") #gets the current screenshot number
    image.save(f'images/screenshot{screenShotNum}.png')
    return f'images/screenshot{screenShotNum}.png'




