
from collections import Counter
from os import startfile
from typing import Counter


def generateSequence(charList, keySize, finalDict):
    # to establish each sequences
    keylength = keySize
    numberOfChars = len(charList)
    valueList = list()

    sequence = 1
    while sequence <= keylength:

        seq = ""
        index = sequence-1
        while(index < numberOfChars):
            seq = seq+charList[index]
            index = index+keylength
        sequence = sequence+1
       # print(seq)
        avgValue = calculteFrequency(seq, keylength, valueList)
        valueList.append(avgValue)

    avgValueforKey = sum(valueList)/len(valueList)
    finalDict.update({keylength: avgValueforKey})

    # ======================================================================================

# now we have to calculate the each letter frequency and add that frequency to the dictionary for each sequence


def calculteFrequency(stringLine, keylength, valueList):
    strFreq = dict()  # to store the frequencies
    for chars in stringLine:
        strFreq[chars] = strFreq.get(chars, 0)+1

    avgvalue = ICvalueCalculation(strFreq, stringLine, keylength, valueList)
    return avgvalue
    # now we have to calculate the IC value for each dictionary sequence


# ================================================================================================
def ICvalueCalculation(sequenceDict, sequence, keylength, valueList):

    # for the calculation

    wordLength = len(sequence)
    total = 0

    for key in sequenceDict:
        total = total+(sequenceDict[key]*(sequenceDict[key]-1))
        # for each sequence we have to add this total value to a list for average calculation at the end
    return total/(wordLength*(wordLength-1))


# ===========================================================================================================


# ========================================================================================
# to get the next frequency

def nextSeq(letterCosets):
    # this function will provide the next sequence for chi analysing process
    newSeq = list()

    for letters in letterCosets:
        upperletter = letters.upper()
        newchar = (chr((ord(upperletter) - 1 + 65) % 26 + 65))
        newSeq.append(newchar.lower())
    return newSeq


# ===========================================================================================================

# we have to do the frequency analysing according to the chi square analyzing method
# get each letter dicpher it with all 26 letter and do the frequency analysing part

def getChiValues(letterCosetslist):

    # then we have to calculate the IC of the cyper text between 2 to 16 sequence
    # this is the theorotical frequency of each letter in alphabet
    freqList = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015, 0.06094, 0.06966, 0.00153, 0.00772, 0.04025,
                0.02406, 0.06749, 0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758, 0.00978, 0.0236, 0.0015, 0.01974, 0.00074]

    a9 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
          'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    # convert above two list into single dictionry
    freqDict = dict()
    for keys in a9:
        for values in freqList:
            freqDict[keys] = values
            freqList.remove(values)
            break

    # print(freqDict)

    letterFreq = dict()  # to store the each letter frequency
    for chars in letterCosetslist:
        letterFreq[chars] = letterFreq.get(chars, 0)+1

    chitotal = 0

    for characters in letterCosetslist:
        chitotal = chitotal+((letterFreq[characters]-freqDict[characters]*len(
            letterCosetslist))**2)/(freqDict[characters]*len(letterCosetslist))

        # now we have to do the ceaser ciper to this leter by reducing it by 1 shift

    return chitotal
# ================================================================================================
# function to store the keys
def keyFinder(chiValuedict):
    #we have to find the key for the minimum value in this dictionry
    
    temp=min(chiValuedict.values())
    minKey=[key for key in chiValuedict if chiValuedict[key] == temp] 
    #print(minKey)
    #letter=chr(minKey+98)
    letter=chr(minKey[0]+97)
    possibleKey.append(letter)
    # =================================================================================================


def chiCalculator(letterCosetslist):
    # we get a list with keys when this function call,so we have to do the chi square statistics
    # we also need the each letter frequency distribution as a dictioanry too
    i = 0
    chitot = 0
    newSequence = list()
    chiValues = dict()
    while i < 26:

        chitot = getChiValues(letterCosetslist)
        #print(letterCosetslist)
        chiValues.update({i: chitot})
        i = i+1
        newSequence = nextSeq(letterCosetslist)
        letterCosetslist = newSequence

    #print("============================================================")
    keyFinder(chiValues)
    #print(chiValues)
    #print("============================================================")
# =================================================================================================


# first lets get the letter cosets
def letterCosets(key):
    fileHandler5 = open("input.txt", "r")
    letters = list()
    letterCosetList = list()
    for line in fileHandler5:
        for chars in line:
            letters.append(chars)

    #print(len(letters), "=========")
    i = 0
    while i < key:
        j = i
        while j < len(letters):

            letterCosetList.append(letters[j])
            j = j+key

        i = i+1
        # when it came down to here it get the one word closet inside the list
        # now we can pass this word for chi frequency analysis and store the chi value along with the sequence
        # print(letterCosetList)
        chiCalculator(letterCosetList)
        letterCosetList.clear()


# main driver ==========================
# ==================================================================================
# first we have to import the encrypted file to the program
fileName = 'input.txt'

try:
    fileHandler = open(fileName, 'r')
except:
    print("File is missing or incorrect file name!")
    quit()


# to append each charater to the list from the encrypted text
charList = list()
for line in fileHandler:
    for characters in line:
        charList.append(characters)
# ====================================================================
finalDict = dict()
keySize = 1
while keySize <= 16:
    generateSequence(charList, keySize, finalDict)
    keySize = keySize+1

fileHandler.close()
# now we got every IC value for each key length
# now we have to find the maximum values from the dictionary for keylength
k = Counter(finalDict)
# store the most 3 maximum values from the IC list
maxValues = k.most_common(3)

dicta = list()
for i in maxValues:
    for j in i[0:1]:
        dicta.append(j)
    dicta.sort()
print(dicta)

# ======================================================================================================================
# now we know the word size of the key now ewe have to find the key that used for the encryption
# we have to import the dictionary and have to find the word that have the same length that we find before


try:
    fileHandler3 = open("dictionary.json", "r")
except:
    print("File is missing or invalid file name!")
    quit()


# now we have to get each and every word in to a list from the dictionary
# string slicing process
dictionaryList = list()

for line in fileHandler3:
    word = line.split(':')
    # now we have to remove quatation marks from each word
    neWword = str(word[0])
    neWword.strip()
    dictionaryList.append(neWword[3:len(neWword)-2])


# now we got the word list from the jason file
# now we have to find the words that suitable for our Maximum IC values
suitableWord = list()


fileHandler4 = open("suitWords.txt", "w")

for i in dicta:
    for travwords in dictionaryList:
        if i == len(travwords):
            fileHandler4.write(travwords+"\n")
fileHandler4.close()

# now we have save all the suitable word with new txt file called suitWords.txt
# we can bring each word from that file and decrypt the cipher text with that.
# for the easyness lets assume the key length is 7 so we have to get the letter cosets
# we can apply chi square method to do the frequency analysis

possibleKey = list()

letterCosets(16)
print(possibleKey)
