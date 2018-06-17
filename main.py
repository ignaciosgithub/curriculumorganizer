import os
import numpy as np
from readfromgmail import read_email_from_gmail
import readfromgmail
running = True
fields = []
categories = []
formm = ""
subj = ""
mailtext = ""
candidatefields = []
currentdir = ""
previousfrom = ""
previoussubj = ""
alreadymarkedfields = []
class Candidate:
    canfields = []
   

for fol in os.listdir('.'):
    if "field" in fol:
        fields.append(fol.replace("field","",1))
for cat in os.listdir('.'):
    if "category" in cat:
        categories.append(cat.replace("category","",1))

print fields
print categories
while running == True:
   fromm,subj,mailtext = read_email_from_gmail()
   if(subj in categories):
       currentdir = os.path.dirname(os.path.abspath(__file__))+"\\category"+subj+"\\"
   else:
       continue
   if previousfrom == fromm and previoussubj == subj:
       continue
   for a in mailtext.split("\n"):    
       for f in fields:
           if f in a:
            candidatefields.append(a)
   canfile = open(currentdir+fromm.replace("<","").replace(">","")+".txt","w")  
   for a in candidatefields:
       canfile.write(a)
   canfile.close()
   previousfrom = fromm    
   previoussubj = subj      
   print candidatefields
   candidatefields = []
   alreadymarkedfields = []
