import joblib
import numpy
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sms
df=pd.read_csv("D:/academic_projects\Breast-cancer-prediction-ML-Python-master\corona_tested_individuals_ver_006.english.csv")
df['cough']=df['cough'].astype(float)
df['fever']=df['fever'].astype(float)
df['sore_throat']=df['sore_throat'].astype(float)
df['shortness_of_breath']=df['shortness_of_breath'].astype(float)
df['head_ache']=df['head_ache'].astype(float)

print(df)
print(df.isna().sum())
print(df.shape)
df=df.dropna(axis=1)
print(df.shape)
print(df.describe())

print(df.head())
age_map = {'age_60_and_above':0}

df_transformed = df.drop('age_60_and_above', axis=1).replace(age_map).add_suffix('1')
df = df.join(df_transformed)

# sms.heatmap(df,cmap='viridis')
# plt.show()
print(df['corona_result'].value_counts())
from sklearn.preprocessing import LabelEncoder
label_en_y=LabelEncoder()
# x1={'cough':'float','fever':'float','sore_throat':'float','shortness_of_breath':'float','head_ache':'float'}
# df=df.astype(x1)
df.iloc[:,6]=label_en_y.fit_transform(df.iloc[:,6].values)


print(df.head())
# df.iloc[:,1:6]=df.iloc[:,1:6].astype(float)
df.iloc[:,1:5]=df.iloc[:,1:5].values

x=df.iloc[:,1:5].values



y=df.iloc[:,6].values
print(y)
print(x)
from sklearn.model_selection import train_test_split
Xtrain,Xtest,Ytrain,Ytest=train_test_split(x,y,test_size=0.20,random_state=0)
from sklearn.preprocessing import StandardScaler


Xtrain=StandardScaler().fit(Xtrain)
Xtest=StandardScaler().fit(Xtest)
# def logModel(Xtrain,Ytrain):
#     from sklearn.linear_model import LogisticRegression
#     log=LogisticRegression(random_state=0)
#     log.fit(Xtrain,Ytrain)
#     from sklearn.tree import  DecisionTreeClassifier
#     tree=DecisionTreeClassifier(random_state=0,criterion="entropy")
#     tree.fit(Xtrain,Ytrain)

#     from sklearn.ensemble import RandomForestClassifier
#     forest=RandomForestClassifier(random_state=0,criterion="entropy",n_estimators=10)

#     forest.fit(Xtrain,Ytrain)
#     print("logistic",log.score(Xtrain,Ytrain))
#     print("Decision",tree.score(Xtrain,Ytrain))
#     print("RandomForest",forest.score(Xtrain,Ytrain))
#     plt.pcolor(log.score(Xtrain,Ytrain))
#     plt.show()
#     return log,tree,forest

# model=logModel(Xtrain,Ytrain)    
# from sklearn.metrics import accuracy_score
# from sklearn.metrics import classification_report 






# for i in range(len(model)):
#     print("model",i)
#     print(classification_report(Ytest,model[i].predict(Xtest)))
#     print("Accurary: ",accuracy_score(Ytest,model[i].predict(Xtest)))
# pred=model[2].predict(Xtest)    

# from joblib import dump
# dump(model[2],"covid19_md.joblib")
  
# model2=joblib.load('D:/academic_projects\Breast-cancer-prediction-ML-Python-master\covid19_md.joblib')
# prd=model2.predict(Xtest)[5]
# if prd==1:
#     print("positive")
# elif prd==0:
#     print("Negitive")    




