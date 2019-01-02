import sys
import os
sys.path.append(os.path.abspath("/home/iiita/Banihali/Intership/Shortlist"))
from split_into_sentence import *
import re
from collections import defaultdict
import spacy
nlp = spacy.load('en')
doc = open('data.txt').read()
doc0 = nlp(doc)

doc1 = re.split('[\t\n]+', doc)
users = {}
key = "User ID"
for entry in doc1:
    if entry.isdigit():
        key = entry

    else:
        users.setdefault(key, []).append(entry)
#print(users)


new_users = {}
for user in users:
    #print(user)
    for i in range(0,2):
        for sentence in split_sent(users[user][i]):
            new_users.setdefault(user, []).append(sentence)


for user in new_users:
    print(user)
    for s in new_users[user]:
        print("\" "+ s + " \" ")



