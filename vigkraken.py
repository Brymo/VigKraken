#Author: Brymo
#Discerns key from vignere encrypted text
#Outputs to STDOUT


def getKeyLen():
   mylist = []
   ICList = []

   for i in range(0,26):
      mylist.append(0)

   colLength = 0.0
   textLength = 0.0
   ICSum = 0.0


   for keyLen in range(1,20):

      for col in range(0,keyLen):
         file = open("encrypted.txt","r")

         for line in file:
            for ch in line:
               if textLength % keyLen == col:
                  mylist[ord(ch)-ord('A')] += 1
                  colLength += 1
 
               textLength += 1

         sum = 0.0
         for num in mylist:
            sum += num*(num-1)

         ICSum += (sum)/((colLength*(colLength-1))/26)

         colLength = 0.0
         file.close()
         textLength = 0.0

         for i in range(0,26):
            mylist[i] = 0     

      ICList.append(ICSum/keyLen)
      ICSum = 0.0


   keyLength = -1
   maxIC = -1
   index = 1

   for IC in ICList:
      if IC > maxIC:
         maxIC = IC
         keyLength = index

      index += 1


   return keyLength

def englishFrequencies():
   freqDict = {
      'A': 8.167,
      'B': 1.492,
      'C': 2.782,
      'D': 4.253,
      'E': 12.702,
      'F': 2.228,
      'G': 2.015,
      'H': 6.094,
      'I': 6.966,
      'J': 0.153,
      'K': 0.772,
      'L': 4.025,
      'M': 2.406,
      'N': 6.749,
      'O': 7.507,
      'P': 1.929,
      'Q': 0.095,
      'R': 5.987,
      'S': 6.327,
      'T': 9.056,
      'U': 2.758,
      'V': 0.978,
      'W': 2.360,
      'X': 0.150,
      'Y': 1.974,
      'Z': 0.074

   }
   return freqDict

def getFrequencies(column):
   freq = {}
   colsize = 0.0
   for i in range(0,26):
      freq[chr(ord('A')+i)] = 0.0

   for ch in column:
      freq[ch] += 1.0

      colsize += 1.0

   for key in freq:
      freq[key] = (freq[key]/colsize)*100.0

   return freq
     

def getColumn(fileName,columnNum, keyLen):
   filer = open(fileName,"r")
   col = []
   count = 0
   for line in filer:
      for ch in line:
         if count % keyLen == columnNum:
            col.append(ch)
         count += 1

   return col

def decryptColumn(column, key):
   decrypted = []
   for ch in column:
      letter = chr(((ord(ch) - ord(key)) % 26) + ord('A'))
      decrypted.append(letter)

   return decrypted


      

def getDeviationFromEnglish(decryptedFrequencies):

   dev = 0.0

   normalFreq = englishFrequencies()

   for key in decryptedFrequencies:
      dev += abs(decryptedFrequencies[key]-normalFreq[key])

   return dev/26.0


def mostLikelyKeyChar(deviations):
   lowestDeviation = 9999
   lowestKey = '!'
   for key in deviations:
      if deviations[key] < lowestDeviation:
         lowestDeviation = deviations[key]
         lowestKey = key
   return lowestKey


   
kLen = getKeyLen()
for col in range(0,kLen):

   column = getColumn("encrypted.txt", col, kLen)
   deviations = {}
   for char in range(0,26):
      potentialKey = chr(ord('A')+char)
      decryptAttempt = decryptColumn(column,potentialKey)
      decrFrequencies = getFrequencies(decryptAttempt)
      deviations[potentialKey] = getDeviationFromEnglish(decrFrequencies)
   print(mostLikelyKeyChar(deviations))
   deviations = {}
            


