# -*- coding: utf-8 -*-


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn import metrics 
from sklearn.ensemble import RandomForestClassifier  
from sklearn.neighbors import KNeighborsClassifier
from sklearn import tree
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import AdaBoostClassifier 
from sklearn.ensemble import GradientBoostingClassifier 
from sklearn.ensemble import BaggingClassifier 
import csv

stopwords =['a', 'about', 'an', 'and', 'are', 'as', 'at', 'be', 'been', 'but', 'by', 'can', \
             'even', 'ever', 'for', 'from', 'get', 'had', 'has', 'have', 'he', 'her', 'hers', 'his', \
             'how', 'i', 'if', 'in', 'into', 'is', 'it', 'its', 'just', 'me', 'my', 'of', 'on', 'or', \
             'see', 'seen', 'she', 'so', 'than', 'that', 'the', 'their', 'there', 'they', 'this', \
             'to', 'was', 'we', 'were', 'what', 'when', 'which', 'who', 'will', 'with', 'you'] 

    
Value =  "2020-05-19T11:31:08.103542Z	    9 Query	FLUSH PRIVILEGES"
"""
#Log_info
with open('Apps.csv', mode='r') as csv_file:
    csv_reader1 = csv.reader(csv_file, delimiter=',') 
    for row1 in csv_reader1:
        Value=row1
"""
        

df = pd.read_csv('C:/Users/bhawn/Downloads/dataset.csv')
df.dropna(inplace=True) 

'''
blanks = []
for i,lb,rv in df.itertuples():
    if type(rv)==str:
        if rv.isspace():
            blanks.append(i)
df.drop(blanks, inplace=True)
'''

X = df['Query']
y = df['Classfication']
 



def LinearSVC_machine(X , y, data):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.44, random_state=42)
    text_clf_lsvc2 = Pipeline([('tfidf', TfidfVectorizer(stop_words=stopwords)),
                         ('clf', LinearSVC()),
    ])
    text_clf_lsvc2.fit(X_train, y_train) 
    predictions = text_clf_lsvc2.predict(X_test)
    print(metrics.confusion_matrix(y_test,predictions))
    print(metrics.classification_report(y_test,predictions))
    print('\n Accuracy ')
    print(metrics.accuracy_score(y_test,predictions)*100)
    result = text_clf_lsvc2.predict([data])
    return result

def RandomForest_Machine(X, y, data):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.44, random_state=42)
    text_clf_lsvc2 = Pipeline([('tfidf', TfidfVectorizer(stop_words=stopwords)),
                         ('clf', RandomForestClassifier(max_depth=2, random_state=0)),
    ])
    text_clf_lsvc2.fit(X_train, y_train) 
    predictions = text_clf_lsvc2.predict(X_test)
    print(metrics.confusion_matrix(y_test,predictions))
    print(metrics.classification_report(y_test,predictions))
    print('\n Accuracy ')
    print(metrics.accuracy_score(y_test,predictions)*100)
    result = text_clf_lsvc2.predict([data])
    return result 

def KNN_Machine(X, y, data):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.44, random_state=42)
    text_clf_lsvc2 = Pipeline([('tfidf', TfidfVectorizer(stop_words=stopwords)),
                         ('clf', KNeighborsClassifier(n_neighbors=3)),
    ])
    text_clf_lsvc2.fit(X_train, y_train) 
    predictions = text_clf_lsvc2.predict(X_test)
    print(metrics.confusion_matrix(y_test,predictions))
    print(metrics.classification_report(y_test,predictions))
    print('\n Accuracy ')
    print(metrics.accuracy_score(y_test,predictions)*100)
    result = text_clf_lsvc2.predict([data])
    return result
       

def decisiontree_Machine(X, y, data):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.44, random_state=42)
    text_clf_lsvc2 = Pipeline([('tfidf', TfidfVectorizer(stop_words=stopwords)),
                         ('clf', tree.DecisionTreeClassifier()),
    ])
    text_clf_lsvc2.fit(X_train, y_train) 
    predictions = text_clf_lsvc2.predict(X_test)
    print(metrics.confusion_matrix(y_test,predictions))
    print(metrics.classification_report(y_test,predictions))
    print('\n Accuracy ')
    print(metrics.accuracy_score(y_test,predictions)*100)
    result = text_clf_lsvc2.predict([data])
    return result     

def logisticreg_machine(X,y,data):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.44, random_state=42)
    text_clf_lsvc2 = Pipeline([('tfidf', TfidfVectorizer(stop_words=stopwords)),
                         ('clf', LogisticRegression(random_state=0)),
    ])
    text_clf_lsvc2.fit(X_train, y_train) 
    predictions = text_clf_lsvc2.predict(X_test)
    print(metrics.confusion_matrix(y_test,predictions))
    print(metrics.classification_report(y_test,predictions))
    print('\n Accuracy ')
    print(metrics.accuracy_score(y_test,predictions)*100)
    result = text_clf_lsvc2.predict([data])
    return result   

def AdaboostClassifier_machine(X, y, data):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.44, random_state=42)
    text_clf_lsvc2 = Pipeline([('tfidf', TfidfVectorizer(stop_words=stopwords)),
                         ('clf',AdaBoostClassifier(RandomForestClassifier(n_estimators=400, max_features="auto", random_state=0))),
    ])
    text_clf_lsvc2.fit(X_train, y_train) 
    predictions = text_clf_lsvc2.predict(X_test)
    print(metrics.confusion_matrix(y_test,predictions))
    print(metrics.classification_report(y_test,predictions))
    print('\n Accuracy ')
    print(metrics.accuracy_score(y_test,predictions)*100)
    result = text_clf_lsvc2.predict([data])
    return result   

def GradientBoostingClassifier_machine(X,y,data):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.44, random_state=42)
    text_clf_lsvc2 = Pipeline([('tfidf', TfidfVectorizer(stop_words=stopwords)),
                         ('clf',AdaBoostClassifier(GradientBoostingClassifier(n_estimators=700, learning_rate=0.25, max_features=2, max_depth=2, random_state=0))) ,
    ])
    text_clf_lsvc2.fit(X_train, y_train) 
    predictions = text_clf_lsvc2.predict(X_test)
    print(metrics.confusion_matrix(y_test,predictions))
    print(metrics.classification_report(y_test,predictions))
    print('\n Accuracy ')
    print(metrics.accuracy_score(y_test,predictions)*100)
    result = text_clf_lsvc2.predict([data])
    return result     

def BaggingClassifier_machine(X,y,data):
    base_cls =tree.DecisionTreeClassifier()
    num_trees = 600
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.44, random_state=42)
    text_clf_lsvc2 = Pipeline([('tfidf', TfidfVectorizer(stop_words=stopwords)),
                         ('clf',BaggingClassifier(base_estimator = base_cls,  n_estimators = num_trees, random_state = 47) ),
    ])
    text_clf_lsvc2.fit(X_train, y_train) 
    predictions = text_clf_lsvc2.predict(X_test)
    print(metrics.confusion_matrix(y_test,predictions))
    print(metrics.classification_report(y_test,predictions))
    print('\n Accuracy ')
    print(metrics.accuracy_score(y_test,predictions)*100)
    result = text_clf_lsvc2.predict([data])
    return result     

def XGBClassifier(X,y,data):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.44, random_state=42)
    text_clf_lsvc2 = Pipeline([('tfidf', TfidfVectorizer(stop_words=stopwords)),
                         ('clf', GradientBoostingClassifier(n_estimators=20,  max_features=2, max_depth=2, random_state=0) ),
    ])
    text_clf_lsvc2.fit(X_train, y_train) 
    predictions = text_clf_lsvc2.predict(X_test)
    print(metrics.confusion_matrix(y_test,predictions))
    print(metrics.classification_report(y_test,predictions))
    print('\n Accuracy ')
    print(metrics.accuracy_score(y_test,predictions)*100)
    result = text_clf_lsvc2.predict([data])
    return result
    

def credit_function():
    string1 = LinearSVC_machine(X, y, Value)
    string2 = RandomForest_Machine(X,y ,Value)
    string3 = KNN_Machine(X,y , Value)
    string4 = decisiontree_Machine(X,y, Value)
    string5 = logisticreg_machine(X,y, Value)
    string6 = AdaboostClassifier_machine(X,y,Value)
    string7 = GradientBoostingClassifier_machine(X,y,Value)
    string8 = BaggingClassifier_machine(X,y,Value)
    string9 = XGBClassifier(X,y,Value)
    string10 = " "
    string11=['Unauthorised']
    if string1 ==string11 or string2 ==string11 or string3 ==string11 or string4 ==string11 or string5 ==string11 or string6 ==string11 or string7==string11 or string8 ==string11 or string9==string11 :
        string10="Unauthorised Access"
    return string10 

 
def Result ():   
    with open('Result.csv', 'w') as new_file:
        string=credit_function()
        csv_writer = csv.writer(new_file, delimiter=',')
        csv_writer.writerow(['Log_information', 'Access_Status'])
        csv_writer.writerow([Value, string])
        print('\n-----------------------------------------LOG INFORMATION------------------------------------------------')
        print(Value,"-", string, sep='\t')
        print('----------------------------------------------------------------------------------------------------------\n')
        
        
if __name__ == "__main__": 
    Result()
    
     
