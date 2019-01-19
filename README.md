# Shortlist_Scholarships
A mini project perform Information Extraction using NLP toolkit Spacy and decide to select candidates for scholarship.
 Input:- A .txt file containing information of user. 
 
 Output:- A .txt file containing user_id and information of selected users.
 
 Execution:
 
Begins with 'main.py' file where it reads input file.

All the calls are made from this 'main.py' file. Hance decision and output is also genrated in 'main.py'.

Helper Functions:

1.)'split_into_sentences.py': To split the text into sentences called from 'main.py'

2.)'demo.py': To create Spacy feedable data from anotated training data file. Called from 'nettagspacy.py'

3.)'nettagspacy.py': Train and save spacy custom 'NER' model in local directory.

#Tools Used:

Spacy for NLP "https://spacy.io/"

Dataturks for creating Anotated training data "https://dataturks.com/projects"
