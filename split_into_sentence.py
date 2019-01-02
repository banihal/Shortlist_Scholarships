import re
import  spacy
nlp = spacy.load('en')
alphabets= "([A-Za-z])"
prefixes = "(St|[M|m]rs|Mr|Ms|[D|d]r|[A|a]sst|[0-9]|" \
           "[G|g][O|o][V|v][T|t]|Vr|[S|s][K|k]|[B]|[s|S]r|[P|p]h|edu|A|M|CA|yrs|" \
           "BSC|P|bt|bc|Panvani|[C|c][H|h]|J|[S|s]t|Rs|Kalangi|kavitha|YACHAVARAPU|Sreelakshmi |v |Sc|G)[.]"
suffixes = "(Inc|Ltd|Jr|Sr|Co|Pvt)"
starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
websites = "[.](com|net|org|io|gov)"
errors = ""
def split_sent(text):

    text = " " + text + "  "
    text = text.replace("\n"," ")
    text = re.sub(prefixes,"\\1<prd>",text)
    text = re.sub(websites,"<prd>\\1",text)
    if "Ph.D" in text: text = text.replace("Ph.D.","Ph<prd>D<prd>")
    if "p.m" in text: text = text.replace("p.m", "p<prd>m<prd>")
    if "i.e" in text: text = text.replace("i.e", "i<prd>e<prd>")
    if ".." in text: text = text.replace("..", "<prd><prd>")
    if "!!" in text: text = text.replace("!!", "<prd><prd>")
    text = re.sub("\s" + alphabets + "[.] "," \\1<prd> ",text)
    text = re.sub(acronyms+" "+starters,"\\1<stop> \\2",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>",text)
    text = re.sub(" "+suffixes+"[.] "+starters," \\1<stop> \\2",text)
    text = re.sub(" "+suffixes+"[.]"," \\1<prd>",text)
    text = re.sub(" " + alphabets + "[.]"," \\1<prd>",text)
    if "”" in text: text = text.replace(".”","”.")
    if "\"" in text: text = text.replace(".\"","\".")
    if "!" in text: text = text.replace("!\"","\"!")
    if "?" in text: text = text.replace("?\"","\"?")
    if ".." in text: text = text.replace("..\"", "\"..")
    text = text.replace(".",".<stop>")
    text = text.replace("?","?<stop>")
    text = text.replace("!","!<stop>")
    text = text.replace("<prd>",".")
    sentences = text.split("<stop>")
    sentences = sentences[:-1]
    sentences = [s.strip() for s in sentences]
    return sentences

#text = open('data.txt').read()
#sentences = split_into_sentences(text)
#for sent in sentences:
    #print("\"" + sent + "\"")





