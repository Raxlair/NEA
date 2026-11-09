import jisho_api.tokenize, jisho_api.word

def sentenceSplitter(sentence):
    sentenceList = []
    result = jisho_api.tokenize.Tokens.request(sentence) #stores the result as a list of objects of the class Token
    for word in result:
        sentenceList.append(word.token) #appends the each word in the sentence to the list sentenceList
    return sentenceList

def lookup(word):
    wordInfoDict = {
        "word": "",
        "reading": "",
        "meaning": "",
        "frequency": "",
    }
    result = jisho_api.word.Word.request(word)
    wordInfoDict["word"] = result.data[0].japanese[0].word #string
    wordInfoDict["reading"] = result.data[0].japanese[0].reading #sting
    wordInfoDict["meaning"] = result.data[0].senses[0].english_definitions #list of strings
    #wordInfoDict["frequency"] = result.data[0].jlpt[0] #sting
    return wordInfoDict