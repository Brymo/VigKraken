#Author: Brymo
#Takes in text from hpt.txt and converts it into encryptable format.
#Outputs to cryptReady.txt

filer = open("hpt.txt","r")
filew = open("cryptReady.txt", "w")

for line in filer:
   for ch in line:
      if ch >= 'a' and ch <= 'z':
         filew.write(ch.upper())
      elif ch >= 'A' and ch <= 'Z' :
         filew.write(ch)


filer.close()
filew.close()



