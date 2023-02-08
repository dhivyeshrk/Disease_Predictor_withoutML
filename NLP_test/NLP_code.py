from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer

# from nltk.tokenize import

lemmatizer = WordNetLemmatizer()
splitter = RegexpTokenizer(r'\w+')
user_input=input("Enter symptoms by separating with commas\n").lower().split(",")
processed_symptoms=[]
for sym in user_input:
    sym=sym.replace("-"," ")
    sym=sym.replace("'","")
    sym=' '.join([lemmatizer.lemmatize(word) for word in splitter.tokenize(sym) ])
    processed_symptoms.append(sym)

print(processed_symptoms)