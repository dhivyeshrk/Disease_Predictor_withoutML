# Create your views here.


from django.shortcuts import render
from nltk import WordNetLemmatizer, RegexpTokenizer
from django.conf import settings


def index(request):
    return render(request, 'predict/index.html')


def resultpage(request):
    testData = request.GET.get('symptoms', 'default')
    print(testData)

    symptoms = testData.split(',')

    lemmatizer = WordNetLemmatizer()
    splitter = RegexpTokenizer(r'\w+')

    #########################################
    import pandas as pd

    with open("predict/static/Symptoms_list.csv", "r", encoding="utf-8") as f:
        Symptom_list = f.readlines()
    res = []
    for sy in Symptom_list:
        res.append(sy[:len(sy) - 1])

    Symptom_list = res
    Symptom_list = set(Symptom_list)
    df = pd.read_csv("predict/static/Diseases_and_Symptoms_final.csv")
    tem = df.copy()
    head_df = df.head()
    # symptoms = ["depression"]
    test = df.groupby(['diseases'])
    # print("understanding goup by property")
    # print(test)

    # print(symptoms)
    df["sum"] = df[symptoms].sum(axis=1)
    # except Exception:
    #     pass
    t = df.groupby(['sum'], sort=True)
    s = df.nlargest(10, "sum").sort_values('sum', ascending=False)
    min_df = s
    most_df = s

    while min_df['sum'].std() >= 5:
        min_df = min_df[:-1]
    most_df = min_df
    while most_df['sum'].std() >= 2:
        most_df = most_df[:-1]

    most_probable_dis = most_df['diseases'].to_numpy()
    less_probable_dis = [i for i in min_df['diseases'].to_numpy() if i not in most_probable_dis]

    print(f"Most probable diseases : {most_probable_dis}")
    print(f"Less probable disease : {less_probable_dis}")

    #  DRUGS EXTRACTION
    df = pd.read_csv("predict/static/Med_Dis.csv", index_col="disease")
    df.fillna(0, inplace=True)
    Medications = {}

    for disease in most_probable_dis:
        d = df.loc[disease].tolist()
        med_temp = list(filter(lambda x: x != 0, d))
        Medications[disease] = med_temp
    print(Medications)

    print()

    #  TESTS AND PROCEDURES EXTRACTION
    df = pd.read_csv("predict/static/Dis_Tests.csv", index_col="disease")
    df.fillna(0, inplace=True)
    Tests_Procedures = {}

    for disease in most_probable_dis:
        d = df.loc[disease].tolist()
        t_p = list(filter(lambda x: x != 0, d))
        Tests_Procedures[disease] = t_p
    print(Tests_Procedures)

    #  DRUGS EXTRACTION
    df = pd.read_csv("predict/static/Med_Dis.csv", index_col="disease")
    df.fillna(0, inplace=True)
    Medications = {}

    for disease in most_probable_dis:
        d = df.loc[disease].tolist()
        med_temp = list(filter(lambda x: x != 0, d))
        Medications[disease] = med_temp
    print(Medications)

    print()

    #  TESTS AND PROCEDURES EXTRACTION
    df = pd.read_csv("predict/static/Dis_Tests.csv", index_col="disease")
    df.fillna(0, inplace=True)
    Tests_Procedures = {}

    for disease in less_probable_dis:
        d = df.loc[disease].tolist()
        t_p = list(filter(lambda x: x != 0, d))
        Tests_Procedures[disease] = t_p
    print(Tests_Procedures)

    # print(Tests_Procedures)
    dic = {'MostProbableDisease': most_probable_dis, 'LeastProbableDisease': less_probable_dis,
           'disease1': Medications[str(most_probable_dis[0])]}

    dic2 = {'disease1': Medications[str(most_probable_dis[0])]}

    return render(request, 'predict/resultpage.html', dic)

