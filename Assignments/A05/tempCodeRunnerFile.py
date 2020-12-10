chitotal=0
    
    for characters in letterCosetslist:
        chitotal=chitotal+((letterFreq[characters]-freqDict[characters]*len(letterCosetslist))**2)/(freqDict[characters]*len(letterCosetslist))