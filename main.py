import screenshot, ocr, lookup, audio, files, anki

textBox = (100, 500, 1200, 700)
game = "Steins;Gate"

#audioPath = audio.captureSentenceAudio(game)
audioPath = "haha"
imagePath = screenshot.takeScreenshot(game)
sentence = ocr.OCR(imagePath, textBox)
sentenceList = lookup.sentenceSplitter(sentence)
print(sentenceList)
resultDict = lookup.lookup(sentenceList[0])
anki.addCard(anki.getDeck(2), anki.getNoteType(14), resultDict, audioPath, sentence, imagePath)



""" imagePath = screenshot.takeScreenshot(game)
sentence = ocr.OCR(imagePath, textBox)
sentenceList = lookup.sentenceSplitter(sentence)
print(lookup.lookup(sentenceList[0]))
audio.captureSentenceAudio(game) """