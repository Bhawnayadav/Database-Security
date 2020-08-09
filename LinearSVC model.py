# -*- coding: utf-8 -*-
"""
Created on Sun May 24 2020

@author: bhawn
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn import metrics 

data="2020-05-19T11:29:45.986082Z	    6 Query	set @is_mysql_encrypted = (select ENCRYPTION from information_schema.INNODB_TABLESPACES where NAME='mysql');"



 
stopwords = ['a', 'about', 'an', 'and', 'are', 'as', 'at', 'be', 'been', 'but', 'by', 'can', \
             'even', 'ever', 'for', 'from', 'get', 'had', 'has', 'have', 'he', 'her', 'hers', 'his', \
             'how', 'i', 'if', 'in', 'into', 'is', 'it', 'its', 'just', 'me', 'my', 'of', 'on', 'or', \
             'see', 'seen', 'she', 'so', 'than', 'that', 'the', 'their', 'there', 'they', 'this', \
             'to', 'was', 'we', 'were', 'what', 'when', 'which', 'who', 'will', 'with', 'you']
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
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
text_clf_lsvc2 = Pipeline([('tfidf', TfidfVectorizer(stop_words=stopwords)),
                     ('clf',  LinearSVC()),
])
text_clf_lsvc2.fit(X_train, y_train) 
predictions = text_clf_lsvc2.predict(X_test)
print(metrics.confusion_matrix(y_test,predictions))
print(metrics.classification_report(y_test,predictions))
print(metrics.accuracy_score(y_test,predictions))
result = (text_clf_lsvc2.predict([data]))
print(result) 

