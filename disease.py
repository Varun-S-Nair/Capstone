def getRankings(condition):
    import numpy as np
    import random
    import warnings
    warnings.filterwarnings('ignore')
    import pandas as pd
    df = pd.read_csv('/home/prabhar2042/mysite/medium_clean.csv')
    df = df.drop(['Unnamed: 0'], axis = 1)
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier
#     from sklearn.preprocessing import StandardScaler
    x_cols = ["drugID"]
    y_col = ["rating"]
    test_size = 0.2
    random_state = 3
    x_train,x_test,y_train,y_test = train_test_split(df[x_cols],df[y_col],test_size=test_size, random_state=random_state)

    model = RandomForestClassifier(n_estimators=12)
#     start = time.time()
#     print(model.__class__.__name__)
    #         print(y_train.values.ravel()[:13])
    model.fit(x_train,y_train)
    # y_train_pred= model.predict(x_train)
    #     print("Real: ", np.array(y_train[:13]))
    #     print("Predicted: ", y_train_pred[:13])
    #     print("Training Accuracy: ", accuracy_score(y_train, y_train_pred)*100)
#     print("Training Accuracy: ", checkAcc(np.array(y_train), np.array(y_train_pred), i)*100)
    # y_pred = model.predict(x_test)
    #     print("Testing Accuracy: ", accuracy_score(y_test, y_pred)*100)
    #     print("Real: ", np.array(y_test[:13]))
    #     print("Predicted", y_pred[:13])
#     print("Testing Accuracy: ", checkAcc(np.array(y_test), np.array(y_pred), i)*100)
#     elapsed = time.time()-start
#     print("Time: " + str(elapsed/60) + " minutes, or " + str(elapsed) + " seconds.")
    import operator
    def getDrugs(condition):
        return np.unique(np.array(df[df['condition']==condition]["drugName"]))

    def getRating(drug):
        df2 = df[df['drugName']==drug]["drugID"].iloc[0]
        test = pd.DataFrame(np.array([df2]))
        return round(model.predict(test)[0]*10*(random.random()*0.1+0.9), 2)

    graph = {}

    for i in getDrugs(condition):
        graph[i] = getRating(i)
    graph = sorted(graph.items(), key=operator.itemgetter(1))
    graph = graph[::-1][:5]
    return graph



def getRecommendation(symptoms):
    import pandas as pd
    import operator
    df_disease = pd.read_csv('/home/prabhar2042/mysite/dia_t_clean.csv', encoding='latin-1')
    df_symptoms = pd.read_csv('/home/prabhar2042/mysite/sym_t.csv')
    df_dis_sym_c = pd.read_csv('/home/prabhar2042/mysite/disease_symptom_with_Vineet.csv', encoding='latin-1')
    df_dis_sym_c = df_dis_sym_c.drop(columns=['Unnamed: 0'], axis=1)
    symp_dict = {}
    for i in range(len(df_symptoms)):
        symp_dict[df_symptoms.iloc[i, 0]] = df_symptoms.iloc[i, 1]
    symp_dict2 = {}
    for i in range(len(df_symptoms)):
        symp_dict2[df_symptoms.iloc[i, 1]] = df_symptoms.iloc[i, 0]
    dis_dict = {}
    for i in range(len(df_disease)):
        dis_dict[df_disease.iloc[i, 0]] = df_disease.iloc[i, 1]
    dis_dict2 = {}
    for i in range(len(df_disease)):
        dis_dict2[df_disease.iloc[i, 1]] = df_disease.iloc[i, 0]

    def return_disease(symptoms):
        top_five = []
        value_lst = []
        per_match_dic = {}
        for row in range(len(df_dis_sym_c)):
            match = 0
            total = 0
            lst = df_dis_sym_c.iloc[row, 1]
            for symptom in symptoms:
                if str(symp_dict2[symptom]) in lst:
                    match += 1
                    total += 1
                else:
                    total += 1
            per_match = match/total
            disease_index = df_dis_sym_c.iloc[row, 0]
            disease = dis_dict[disease_index]
            per_match_dic[disease] = per_match
        for value in per_match_dic.values():
            value_lst.append(value)
        value_lst = sorted(value_lst)
        value_lst_top = value_lst[-1:-6:-1]
        for disease, value in per_match_dic.items():
            if value in value_lst_top:
                top_five.append((disease, value))
        return top_five
    #returns top five only, no ties
    dis_lst = return_disease(symptoms)
    dis_dic = dict(dis_lst)
    for i in dis_dic:
        dis_dic[i] = round(dis_dic[i], 2)
    dis_dic.update((x, y*100) for x, y in dis_dic.items())
    dis_dic = sorted(dis_dic.items(), key=operator.itemgetter(1))
    dis_dic = dis_dic[::-1][:5]
    dis_dic = dict(dis_dic)
    for i in dis_dic:
        dis_dic[i] = str(dis_dic[i]) + '% match'
    s = ""
    for i in dis_dic:
        s += i + " (" + dis_dic[i] + "), "
    s = s[:-2]
    return s







