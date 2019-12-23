import dictionary

lastType = ''
lastIndex = ''

def printTag(index, word, char):
    print('{' + char + '-' + dictionary.dictionary[index]['tag'] + '}' + word)


def cleanName(oldName):
    newName =  oldName.split('\'')[0]
    newName =  newName.replace('"','')
    return  newName.split('’')[0]

def searchInSubDict(name, searchThing):
    searchThing = cleanName(searchThing)
    global lastType
    global lastIndex
    has = 0
    for i in range(len(dictionary.dictionary[name]['words'])):
        splitedDictWord = dictionary.dictionary[name]['words'][i].split(' ')
        for j in range(0, len(splitedDictWord)):
            if splitedDictWord[j] == searchThing and (lastIndex==i or j==0) :
                has = 1
                break
        if has == 1:
            if lastType == '':
                lastType = name
                lastIndex = i
                printTag(name, searchThing, 'B')
            elif lastType != name:
                printTag(name, searchThing, 'B')
                lastIndex = i
            elif lastType == name and lastIndex == i:
                printTag(name, searchThing, 'I')
            return 1
    return 0

def findInDictionary(twitWord, afterWords=[]):
    global lastType,lastIndex
    response = 0
    response += searchInSubDict('SpecialName', twitWord)
    response += searchInSubDict('Organization', twitWord)
    response += searchInSubDict('Location', twitWord)
    response += searchInSubDict('Date', twitWord)
    if response==0:
        lastIndex=-1
        lastType=''

def twitArray(twit):
    twitArr = twit.split(' ')
    global lastType
    lastType = ''
    for i in range(len(twitArr)):
        findInDictionary(cleanName(twitArr[i].lower()))
    print('-----')
