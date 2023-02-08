import pandas as pd
from sklearn.linear_model import LogisticRegression
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer
# nltk.download('wordnet')
from nltk.corpus import wordnet
from sklearn.model_selection import cross_val_score

df_comb = pd.read_csv("dis_sym_dataset_comb.csv")
df_norm = pd.read_csv("dis_sym_dataset_norm.csv")

X = df_comb.iloc[:, 1:]
y = df_comb.iloc[:, 0:1]

lr = LogisticRegression()
lr = lr.fit(X, np.ravel(y))
scores = cross_val_score(lr, X, np.ravel(y), cv=5)

dataset_symptoms = list(X.columns)
lemmatizer = WordNetLemmatizer()
splitter = RegexpTokenizer(r'\w+')

from bs4 import BeautifulSoup
import requests


def synonyms(term):
    synonyms = []
    '''response = requests.get('https://www.thesaurus.com/browse/{}'.format(term))
    soup = BeautifulSoup(response.content,  "html.parser")
    try:
        container=soup.find('section', {'class': 'MainContentContainer'}) 
        row=container.find('div',{'class':'css-191l5o0-ClassicContentCard'})
        row = row.find_all('li')
        for x in row:
            synonyms.append(x.get_text())
    except:
        None'''
    for syn in wordnet.synsets(term):
        synonyms += syn.lemma_names()
    return set(synonyms)


user_input = input("Enter symptoms by separating with commas\n").lower().split(",")
processed_symptoms = []
for sym in user_input:
    sym = sym.replace("-", " ")
    sym = sym.replace("'", "")
    sym = ' '.join([lemmatizer.lemmatize(word) for word in splitter.tokenize(sym)])
    processed_symptoms.append(sym)

print(processed_symptoms)

import combinations

syn_list = []
for sym in processed_symptoms:
    sym_split = sym.split()
    sym_set = {}
    for s in sym_split:
        syn = synonyms(s)
        sym_set.update(syn)
syn_list.append(sym_set)

from itertools import combinations

'''syn_list=[]
for sym in processed_symptoms:
    sym_split=sym.split()
    sym_set=set()
    for comb in range(1,len(sym_split)+1):

     for s in combinations(sym_split,comb):
        s=' '.join(s)
        syn=synonyms(s)
        sym_set.update(syn)
    sym_set.add(' '.join(sym_split))
    syn_list.append(' '.join(sym_set).replace('_',' '))'''
user_symptoms = []
for user_sym in processed_symptoms:
    user_sym = user_sym.split()
    str_sym = set()
    for comb in range(1, len(user_sym) + 1):
        for subset in combinations(user_sym, comb):
            subset = ' '.join(subset)
            subset = synonyms(subset)
            str_sym.update(subset)
    str_sym.add(' '.join(user_sym))
    user_symptoms.append(' '.join(str_sym).replace('_', ' '))
# query expansion performed by joining synonyms found for each symptoms initially entered
print("After query expansion done by using the symptoms entered")
print(user_symptoms)

'''found_sym=[]
for id,val in enumerate(dataset_symptoms):
    val_split=val.split()
    count=0
    for sym in syn_list:
        sym_sp=sym.split()
        for s in sym_sp:
            if s in val_split:
                count+=1
    if (count/len(val_split))>0.5:
            found_sym.append(sym)
found_sym=list(found_sym)'''
found_symptoms = set()
for idx, data_sym in enumerate(dataset_symptoms):
    data_sym_split = data_sym.split()
    for user_sym in user_symptoms:
        count = 0
        for symp in data_sym_split:
            if symp in user_sym.split():
                count += 1
        if count / len(data_sym_split) > 0.5:
            found_symptoms.add(data_sym)
found_symptoms = list(found_symptoms)
print(found_symptoms)

print("Top matching symptoms from your search!")
for idx, symp in enumerate(found_symptoms):
    print(idx, ":", symp)

select = input("Enter symptoms with index number : ").split()
print(select)
sym_matched = []
dis_list = set()
for id in select:
    sym_matched.append(found_symptoms[int(id)])
    sym = found_symptoms[int(id)]
    dis_list.update((df_norm[df_norm[sym] == 1]['label_dis']))
print(sym_matched)
print(dis_list)

counter_list = []
for dis in dis_list:
    row = df_norm[df_norm['label_dis'] == dis].values.tolist()
    row[0].pop(0)
    for id, x in enumerate(row[0]):
        if x != 0 and df_norm.columns[id + 1] not in sym_matched:
            counter_list.append(df_norm.columns[id + 1])
counter_list = set(counter_list)
counter_list = list(counter_list)
print(counter_list)

count = 0
for id, val in enumerate(counter_list):
    count += 1
    if count == 5:
        print("Select symptoms: ")
        for i in range(5):
            print(id - (4 - i), ":", counter_list[id - (4 - i)])
        user_input_sym = input("Enter the symptoms index (or) enter -1 to skip (or) enter '-2' to stop").split()
        if len(user_input_sym) != 1:
            for x in user_input_sym[:-1]:
                sym_matched.append(counter_list[int(x)])

        if int(user_input_sym[-1]) == -1:
            count = 0
            continue
        elif int(user_input_sym[-1]) == -2:
            break

print(sym_matched)

from sklearn.model_selection import train_test_split, cross_val_score

sample = []
for i in range(len(df_norm.columns) - 1):
    sample.append(0)
for id, val in enumerate(dataset_symptoms):
    for sym in sym_matched:
        if sym == val:
            sample[id] = 1
print(sample)

'''prediction = lr.predict_proba([sample])
print(prediction)'''
'''Show top k diseases and their probabilities to the user.

K in this case is 10'''

'''k = 10
diseases = list(set(y['label_dis']))
diseases.sort()
topk = prediction[0].argsort()[-k:][::-1]
print(topk)'''

prediction = lr.predict_proba([sample])
diseases = list(set(y['label_dis']))
diseases.sort()
k = 10
topk = prediction[0].argsort()[-k:][::-1]
print(topk)

import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
from sklearn.model_selection import train_test_split, cross_val_score
from statistics import mean
from nltk.corpus import wordnet
import requests
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer
from itertools import combinations
from time import time
from collections import Counter
import operator

import math

print(f"\nTop {k} diseases predicted based on symptoms")
topk_dict = {}
# Show top 10 highly probable disease to the user.
for idx, t in enumerate(topk):
    match_sym = set()
    row = df_norm.loc[df_norm['label_dis'] == diseases[t]].values.tolist()
    row[0].pop(0)

    for idx, val in enumerate(row[0]):
        if val != 0:
            match_sym.add(dataset_symptoms[idx])
    prob = (len(match_sym.intersection(set(sym_matched))) + 1) / (len(set(sym_matched)) + 1)
    prob *= mean(scores)
    topk_dict[t] = prob
j = 0
topk_index_mapping = {}
topk_sorted = dict(sorted(topk_dict.items(), key=lambda kv: kv[1], reverse=True))
for key in topk_sorted:
    prob = topk_sorted[key] * 100
    print(str(j) + " Disease name:", diseases[key], "\tProbability:", str(round(prob, 2)) + "%")
    topk_index_mapping[j]=key
    j += 1