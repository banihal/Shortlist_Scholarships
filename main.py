import sys
import os
sys.path.append(os.path.abspath("/home/iiita/Banihali/Intership/Shortlist"))
from split_into_sentence import *
import re
from collections import defaultdict
import spacy
output_dir= '/home/iiita/Banihali/Intership/Shortlist/'
nlp2 = spacy.load(output_dir)
nlp = spacy.load('en')
################## DICISION #########################################
def getIncome(sent):
    INCOME = ''
    sent1 = nlp2(sent)
    for ent in sent1.ents:
        if ent.label_ in ('OCCUPATION', 'INCOME', 'MONEY') and INCOME == '':
            #print(ent.text)
            INCOME = sent
    return INCOME


def getFamily(sent):
    FAMILY = ''
    sent1 = nlp2(sent)
    for ent in sent1.ents:
        if ent.label_ in ('FAMILY', 'CONDITION') and FAMILY == '':
            FAMILY = sent
    return FAMILY


def getGoal(sent):
    GOAL = ''
    sent1 = nlp2(sent)
    for ent in sent1.ents:
        if ent.label_ == ('GOAL') and GOAL == '':
            GOAL = sent
    return GOAL

############### RANKING ############################################
def getIncomeRank(INCOME):
    relative = open('relative.txt').read()
    relative = relative.split()
    income_rank = 0
    income = INCOME.split()
    for income_class in income:

        if income_class.lower() in ('late', 'died', 'desease', 'ill', 'no', 'more'):
            income_rank = 10

        elif income_class.lower() in ('housewife', 'homemaker', 'house wife', 'home maker'):
            income_rank = 7

        elif income_class.lower() in ('father', 'mother', 'mom', 'dad', 'worker', 'husband'):
            income_rank = 5

        elif income_class.lower() in ('uncle', 'grandfather', 'brother', 'sister'):
            income_rank = 9


    return income_rank


def getFamilyRank(FAMILY):
    family_rank = 0
    family = FAMILY.split()
    for family_class in family:

        if family_class.lower() == 'poor':
            family_rank = 10

        elif family_class.lower() in ('middle-class', 'middle class', 'mediocre'):
            family_rank = 8

        elif family_class.lower() in ('agricultural', 'typical', 'farming'):
            family_rank = 8

        elif family_class.lower() in ('business','rich'):
            family_rank = 3

    return family_rank


def getGoalRank(GOAL):
    goal_rank = 0
    goal = GOAL.split()

    for goal_class in goal:

        if goal_class.lower() in ('ngo','help','entrepreneur','open',):
            goal_rank = 10

        elif goal_class.lower() in ('officer','ias','ips','ca','rdo','cs'):
            goal_rank = 9

        elif goal_class.lower() in ('research','exam','gate','cat','jee','neet'\
                                    ,'doctor','masters','mba','pg','btech','b.tech','bsc','msc'\
                                    ,'ba','engineer','developer'):
            goal_rank = 8

        elif goal_class.lower() in ('teacher','lecturer','professor','trainer','good job', 'govt job'):
            goal_rank = 6


    return goal_rank


##############  SGMENTATION ###################################333333
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


end_users = {}
for user in new_users:
    #print(user)
    for sent in new_users[user]:
        INCOME = getIncome(sent)
        if len(INCOME) > 0:
            income_rank = getIncomeRank(INCOME)
            end_users.setdefault(user, []).append(income_rank)

        FAMILY = getFamily(sent)
        if len(FAMILY) > 0:
            family_rank = getFamilyRank(FAMILY)
            end_users.setdefault(user, []).append(family_rank)

        GOAL = getGoal(sent)
        if len(GOAL) > 0:
            goal_rank = getGoalRank(GOAL)
            end_users.setdefault(user, []).append(goal_rank)



##################  SHORTLIST  ###############################

final_shortlist = {}
for user in end_users:
    final_shortlist[user] = sum(end_users[user])
    #print(final_shortlist[user])
file1 = open("shortlist.txt","w")
sorted_names = sorted(final_shortlist, key=lambda x: final_shortlist[x],reverse=True)
number = 0
for k in sorted_names:
	if number < 30:
		file1.write(k + "\n")
		file1.write(users[k][0] + "\t")
		file1.write(users[k][1] + "\n")
		number += 1
   
