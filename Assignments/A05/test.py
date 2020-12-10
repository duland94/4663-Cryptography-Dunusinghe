


freqList = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015, 0.06094, 0.06966, 0.00153, 0.00772, 0.04025,
                0.02406, 0.06749, 0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758, 0.00978, 0.0236, 0.0015, 0.01974, 0.00074]

a9 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    # convert above two list into single dictionry
freqDict = dict()
for keys in a9:
    for values in freqList:
        freqDict[keys] = values
        freqList.remove(values)
        break

letterCosetslist=['v', 'u', 'r', 'z', 'j', 'u', 'g', 'r', 'g', 'g', 'u', 'g', 'v', 'g', 'j', 'q', 'k', 'e', 'o', 'a', 'g', 'u', 'g', 'k', 'k', 'q', 'v', 'w', 'q', 'p']

letterFreq = dict()  # to store the each letter frequency
for chars in letterCosetslist:
    letterFreq[chars] = letterFreq.get(chars, 0)+1

chitotal=0
    
for characters in letterCosetslist:
    print(characters,letterFreq[characters],freqDict[characters],len(letterCosetslist))
    chitotal=chitotal+((letterFreq[characters]-freqDict[characters]*len(letterCosetslist))**2)/(freqDict[characters]*len(letterCosetslist))

print(chitotal)