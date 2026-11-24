from py_ankiconnect import PyAnkiconnect
import base64 #so i can convert images into base 64 text so that anki likes it

instance = PyAnkiconnect(default_port=8765) #creates and instance of ankiConnect on port 8765

def getDeck(location):
    deckResult = instance("deckNames")
    print(deckResult[location])
    return deckResult[location]

def getNoteType(location):
    noteResult = instance("modelNames")
    print(noteResult[location])
    return noteResult[location]

def getFields(noteType, location):
    fields = instance(action="modelFieldNames", modelName=noteType)
    print(fields)
    return fields[location]

def addCard(deck, noteType, lookupDict, audio, sentence, image):
    meanings = listIntoBullet(lookupDict["meaning"])
    image = imageIntoAnki(image)
    audio = audioIntoAnki(audio)
    result = instance(action="addNote",
        note={
            "deckName":deck,
            "modelName":noteType,
            "fields": {
                getFields(noteType, 0): lookupDict["word"],
                getFields(noteType, 1): lookupDict["word"]+"["+lookupDict["reading"]+"]",
                getFields(noteType, 3): meanings,
                getFields(noteType, 5): audio,
                getFields(noteType, 6): sentence,
                getFields(noteType, 8): image
            }
        }
    )   

def listIntoBullet(list): #so that the python list can turn into an anki list
    bulletString = "<ul>"
    for word in list:
        bulletString = bulletString + "<li>" + word + "</li>"
    bulletString = bulletString + "</ul>"
    return bulletString

def imageIntoAnki(imagePath): #allows images put in the form so that they can work with anki
    with open(imagePath, "rb") as image: #read as binary
        imageData = base64.b64encode(image.read()).decode("utf-8") #reads the image encodeds it as base64 and then converts it into a python string
    imageFile = instance(action="storeMediaFile", filename=imagePath, data=imageData)
    ankiImage = f'<img src="{imageFile}">'
    return ankiImage

def audioIntoAnki(audioPath): #allows images put in the form so that they can work with anki
    with open(audioPath, "rb") as audio: #read as binary
        audioData = base64.b64encode(audio.read()).decode("utf-8") #reads the image encodeds it as base64 and then converts it into a python string
    audioFile = instance(action="storeMediaFile", filename=audioPath, data=audioData)
    ankiAudio = f'[sound:{audioFile}]'
    return ankiAudio
