from PIL import ImageGrab, ImageChops, ImageDraw
from time import sleep
import win32gui
import files

def takeScreenshot(window):
    hwnd = win32gui.FindWindow(None, window) #finds the window handle for the given window name
    image = ImageGrab.grab(all_screens=True, window=hwnd) #all screen=True so that if it is on a different monitor it will still take the screenshot
    screenShotNum = files.fileCouter("images/screenshotCounter.txt") #gets the current screenshot number
    image.save(f'images/screenshot{screenShotNum}.png')
    return f'images/screenshot{screenShotNum}.png'

def monitorChange(window, doesPictureMove, movementLocation): #parameters of the game and if the screen needs to be drawn on - if not doesPictureMove = False and movementLocation = 0
    hwnd = win32gui.FindWindow(None, window) #same as takeScreenshot()
    imageStatic = ImageGrab.grab(all_screens=True, window=hwnd)

    if doesPictureMove == True:
        draw = ImageDraw.Draw(imageStatic)
        draw.rectangle(movementLocation, fill="black")

        compare = True
    
        while compare == True:
            imageVaried = ImageGrab.grab(all_screens=True, window=hwnd)
            draw2 = ImageDraw.Draw(imageVaried)
            draw2.rectangle(movementLocation, fill="black")
            difference = ImageChops.difference(imageStatic, imageVaried)
            
            if difference.getbbox() is None:
                print("same")
            else:
                print("differenct")
                imageStatic = imageVaried
            sleep(2)       

    else:        
        compare = True
        
        while compare == True:
            imageVaried = ImageGrab.grab(all_screens=True, window=hwnd)
            difference = ImageChops.difference(imageStatic, imageVaried)
            
            if difference.getbbox() is None:
                print("same")
            else:
                print("differenct")
                imageStatic = imageVaried
            sleep(2)
        


#monitorChange("Steins;gate", True, (250,500,1920,800))