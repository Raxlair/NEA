import screenshot, ocr, lookup, audio, files, anki
from PIL import ImageGrab, ImageChops, ImageDraw
import tkinter as tk
from time import sleep
import win32gui

def monitorChange(game, doesPictureMove, movementLocation):
    hwnd = win32gui.FindWindow(None, game) #same as takeScreenshot()
    imageStatic = ImageGrab.grab(all_screens=True, window=hwnd)
        
    if doesPictureMove == True:
        draw = ImageDraw.Draw(imageStatic)
        draw.rectangle(movementLocation, fill="black")
        imageStatic = compare(game, imageStatic, doesPictureMove, movementLocation, hwnd)

    else:
        imageStatic = compare(game, imageStatic, doesPictureMove, movementLocation, hwnd)


def compare(game, imageStatic, doesPictureMove, movementLocation, hwnd):

    imageVaried = ImageGrab.grab(all_screens=True, window=hwnd)
    
    if doesPictureMove == True:
        draw2 = ImageDraw.Draw(imageVaried)
        draw2.rectangle(movementLocation, fill="black")
    
    difference = ImageChops.difference(imageStatic, imageVaried)
        
    if difference.getbbox() is None:
        print("same")
    else:
        print("differenct")
        audioPath = audio.captureSentenceAudio(game)
        imagePath = screenshot.takeScreenshot(game)
        sentence = ocr.OCR(imagePath, textBox)
        label = tk.Label(screen, text=sentence, font=("Yu Gothic", 16))
        label.pack()

        imageStatic = ImageGrab.grab(all_screens=True, window=hwnd)
        if doesPictureMove == True:
            draw2 = ImageDraw.Draw(imageStatic)
            draw2.rectangle(movementLocation, fill="black")
        
               
    screen.after(1000, compare, game, imageStatic, doesPictureMove, movementLocation, hwnd)
    return imageStatic


textBox = (100, 500, 1200, 700)
game = "Steins;Gate"
doesPictureMove = True
movementLocation = (175,500,1920,800)

screen = tk.Tk()
screen.title("Visual Novel Miner")
monitorChange(game, doesPictureMove, movementLocation)
# settingButton = tk.Button(screen, text="Settings")
# settingButton.pack()
screen.mainloop()


# imagePath = screenshot.takeScreenshot(game)
# sentence = ocr.OCR(imagePath, textBox)
# sentenceList = lookup.sentenceSplitter(sentence)
# print(sentenceList)
# resultDict = lookup.lookup(sentenceList[4])
# anki.addCard(anki.getDeck(2), anki.getNoteType(14), resultDict, audioPath, sentence, imagePath)

        
