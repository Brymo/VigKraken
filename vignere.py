#Author: Brymo
#Takes in encryptable text from cryptReady.txt and key from user.  Encrypts using vignere.
#Outputs to encrypted.txt

def merge(a,b):
   letter = (ord(a) + ord(b) - 2*ord('A'))%26
   return chr(letter+ord('A'))

filer = open("cryptReady.txt","r")
filew = open("encrypted.txt", "w")

key = raw_input("Enter the key: ").upper()
count = 0

for line in filer:
   for ch in line:
      charFromKey = key[count%len(key)]
      filew.write(merge(ch, charFromKey))
      count += 1

filer.close()
filew.close()



