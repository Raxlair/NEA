import jisho_api.tokenize, requests

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
    response = requests.get("https://jisho.org/api/v1/search/words", params={"keyword": word})
    result = response.json() #convert the json into python dictionaries

    wordInfoDict["word"] = word #string
    wordInfoDict["reading"] = result["data"][0]["japanese"][0]["reading"] #sting
    wordInfoDict["meaning"] = result["data"][0]["senses"][0]["english_definitions"] #list of strings
    if result["data"][0]["jlpt"] != []: #checks if the word that is passed in has a jlpt level
        wordInfoDict["frequency"] = result["data"][0]["jlpt"] #sting
    else:
        wordInfoDict["frequency"] = ""
    return wordInfoDict
