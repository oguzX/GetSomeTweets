import dictionary, re

lastType = ''
lastIndex = ''


def printTag(index, words):
    point = 0
    char = 'B'
    for word in words:
        print('{' + char + '-' + dictionary.dictionary[index]['tag'] + '}' + word)
        if point == 0:
            point = 1
            char = 'I'


def cleanName(oldName):
    newName = oldName.split('\'')[0]
    newName = newName.replace('"', '')
    return newName.split('’')[0].lower()


def getMaxLengthSentence(sentence):
    maxLength = max(sentence['allLength'])
    for i in range(len(sentence)):
        if (sentence[i]['length'] == maxLength):
            return sentence[i]
    return sentence[0]


def searchInSubDict(name, searchThing):
    global lastType
    global lastIndex

    sentence = {}
    indexCounter = 0
    sentence[indexCounter] = {}
    sentence[indexCounter]['length'] = 0
    sentence[indexCounter]['words'] = []
    sentence['allLength'] = [0]
    for i in range(len(dictionary.dictionary[name]['words'])):
        splitedDictWord = dictionary.dictionary[name]['words'][i].split(' ')
        found = 0
        for j in range(0, len(searchThing)):
            # try:
            #     rulesKeys = dictionary.dictionary['rules'].keys()
            #     index = list(rulesKeys).index(cleanName(searchThing[j]))
            #
            # except ValueError:
            #     print()
            if (cleanName(searchThing[j]) in splitedDictWord and cleanName(searchThing[j]) not in
                    dictionary.dictionary['banned']['words']):
                found = 1
                try:
                    sentence[indexCounter]['length'] = sentence[indexCounter]['length'] + 1
                    sentence[indexCounter]['words'].append(searchThing[j])
                except KeyError:  # this is a new word
                    sentence[indexCounter] = {}
                    sentence[indexCounter]['length'] = 1
                    sentence[indexCounter]['words'] = []
                    sentence[indexCounter]['words'].append(searchThing[j])
        if (found == 1):
            sentence['allLength'].append(sentence[indexCounter]['length'])
            indexCounter += 1
            found = 0

    return getMaxLengthSentence(sentence)


def findInDictionary(twitWord, afterWord=[]):
    global lastType, lastIndex
    response = 0
    sentences1 = searchInSubDict('SpecialName', twitWord)
    sentences2 = searchInSubDict('Organization', twitWord)
    sentences3 = searchInSubDict('Location', twitWord)
    sentences4 = searchInSubDict('Date', twitWord)
    sentences5 = searchInSubDict('Gender', twitWord)

    longestSentence = max(sentences1['length'], sentences2['length'], sentences3['length'], sentences4['length'],
                          sentences5['length'])
    if sentences1['length'] == longestSentence:
        printTag('SpecialName', sentences1['words'])
    if sentences2['length'] == longestSentence:
        printTag('Organization', sentences2['words'])
    if sentences3['length'] == longestSentence:
        printTag('Location', sentences3['words'])
    if sentences4['length'] == longestSentence:
        printTag('Date', sentences4['words'])
    if sentences5['length'] == longestSentence:
        printTag('Gender', sentences5['words'])
    if response == 0:
        lastIndex = -1
        lastType = ''


def twitArray(twit):
    twitArr = twit.split(' ')
    global lastType
    lastType = ''
    findInDictionary(twitArr)
    print('-----')
