import screenshot, ocr, lookup

textBox = (100, 500, 1200, 700)

imagePath = screenshot.takeScreenshot('Steins;Gate')
sentence = ocr.OCR(imagePath, textBox)
sentenceList = lookup.sentenceSplitter(sentence)
print(lookup.lookup(sentenceList[1]))