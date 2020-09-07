################################
# Dulan Dunusinghe
# dulandunusinghe@gmail.com
# CMPS 4663 Cryptography - Dr Griffin
##################################

alphabet = [chr(x+97) for x in range(26)]

class Frequency():
    def __init__(self):
        self.text = ""
        self.freq = {}
        self.sort_freq = None

        for l in alphabet:
            self.freq[l] = 0

    def getNth(self,n):
        if self.sort_freq:
            return self.sort_freq[n][0]        
    
    def count(self,text):
        for l in text:
            l = l.lower()
            if l in alphabet:
                self.freq[l] += 1

        self.sort_freq = sorted(self.freq.items(), key=lambda x: x[1], reverse=True)

    def print(self):
        if self.sort_freq:
            for f in self.sort_freq:
                print(f"{f[0]}:{f[1]}")
        else:
            print(self.freq)

        return None

if __name__=='__main__':
    text = open("ciphertext_1.txt","r").readline()

    F = Frequency()
    F.count(text)
    F.print()
    print(F.getNth(2))
