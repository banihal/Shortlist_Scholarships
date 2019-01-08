import  spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from spacy.tokenizer import Tokenizer
import sys
import os
sys.path.append(os.path.abspath("/home/iiita/Banihali/Intership/Shortlist"))
from split_into_sentence import *
output_dir= '/home/iiita/Banihali/Intership/Shortlist/'
nlp = spacy.load(output_dir)
nlp1 = spacy.load('en')
tokenizer = Tokenizer(nlp.vocab)
stopwords = spacy.lang.en.stop_words.STOP_WORDS
doc1 = open('data.txt').read()
def stopWord(sent):
    stop = []
    nstop = []
    doc = tokenizer(sent)
    for token in doc:
        if token.is_stop or token.lower_ in stopwords or token.lemma_ in stopwords:
            stop.append(token.text)

    for token in doc:
        if token.text not in stop:
            nstop.append(token.text)
    return  nstop

#print(stopWord(doc1))
INCOME = []
EDU = []
FAMILY = []
GOAL = []
nlp2 = spacy.load(output_dir)
sentence = split_sent(doc1)
for sent1 in sentence:
    sent = nlp2(sent1)
    for ent in sent.ents:
        if ent.label_ in ('OCCUPATION', 'INCOME', 'MONEY') and sent not in INCOME:
            #print(ent.text)
            INCOME.append(sent1)
            continue
        if ent.label_ == 'STUDY':
            EDU.append(sent1)

        if ent.label_ in ('FAMILY', 'CONDITION') :
            FAMILY.append(sent1)

        if ent.label_ == ('GOAL') :
            GOAL.append(sent1)

##########G  INCOME  ###################################

relative = open('relative.txt').read()
relative = relative.split()
income_rank = 0
RANK = []
INCOME = set(INCOME)
for income in INCOME:
    income = nlp(income)
    for income_class in income:

        if income_class.lower_ in ('late', 'died', 'desease', 'ill', 'no', 'more'):
            income_rank = 10
            RANK.append(income_rank)
        elif income_class.lower_ in ('housewife', 'homemaker', 'house wife', 'home maker'):
            income_rank = 7
            RANK.append(income_rank)
        elif income_class.lower_ in ('father','mother','mom','dad','worker','husband'):
            income_rank = 5
            RANK.append(income_rank)
        elif income_class.lower_ in ('uncle','grandfather','brother','sister'):
            income_rank = 9
            RANK.append(income_rank)

for rank in RANK:
    print(rank)
##########G  EDUCATION  ###################################

# EDU = set(EDU)
# for ed in EDU:
#     print(ed)

##########G  FAMILY  ###################################
family_rank = 1
RANK = []
FAMILY = set(FAMILY)
for family in FAMILY:
    family = family.split()
    for family_class in family:
        if family_class == 'poor':
            family_rank = 10
            RANK.append(family_rank)
        elif family_class in ('middle-class', 'middle class', 'mediocre'):
            family_rank = 8
            RANK.append(family_rank)
        elif family_class in ('agricultural', 'typical', 'farming'):
            family_rank = 7
            RANK.append(family_rank)
        elif family_class in ('business'):
            family_rank = 6
            RANK.append(family_rank)
        elif family_class in ('rich'):
            family_rank = 3
            RANK.append(family_rank)
for rank  in RANK:
    print(rank)
##########G  GOAL  ###################################
goal_rank = 0
RANK = []
GOAL = set(GOAL)
for goal in GOAL:
    #print(goal)
    goal = goal.split()
    for goal_class in goal:
        if goal_class.lower() in ('ngo','help','entrepreneur','open',):
            goal_rank = 10
            RANK.append(goal_rank)
        elif goal_class.lower() in ('officer','ias','ips','ca','rdo','cs'):
            goal_rank = 9
            RANK.append(goal_rank)
        elif goal_class.lower() in ('research','exam','gate','cat','jee','neet'\
                                    ,'doctor','masters','mba','pg','btech','b.tech','bsc','msc'\
                                    ,'ba','engineer','developer'):
            goal_rank = 8
            RANK.append(goal_rank)
        if goal_class.lower() in ('teacher','lecturer','professor','trainer','good job', 'govt job'):
            goal_rank = 6
            RANK.append(goal_rank)

for rank in RANK:
    print(rank)