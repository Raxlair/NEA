import screenshot, ocr, lookup, audio, files

textBox = (100, 500, 1200, 700)
game = "Steins;Gate"

imagePath = screenshot.takeScreenshot(game)
sentence = ocr.OCR(imagePath, textBox)
sentenceList = lookup.sentenceSplitter(sentence)
print(lookup.lookup(sentenceList[0]))
audio.captureSentenceAudio(game)