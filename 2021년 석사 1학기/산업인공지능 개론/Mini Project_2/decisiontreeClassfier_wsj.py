# -*- coding: utf-8 -*-
"""
Created on Mon May  3 22:31:21 2021

@author: wsj
"""
import matplotlib.pyplot as plt #시각화를 위한 라이브러리
import pandas as pd #파일입출력을 위한 라이브러리
from sklearn.tree import DecisionTreeClassifier, plot_tree #결정트리를 사용을 위한 라이브러리
import numpy as np #배열을 위한 라이브러리
from sklearn import metrics #성능측정을 위한라이브러리
from sklearn.preprocessing import LabelEncoder

#트래커 3일치의 데이터를 획득하여 2일치는 train데이터 1일치는  test데이터로 분리
#train 데이터약 2900ea 테스트 데이터 약 1400ea
train = pd.read_csv('train.csv')     #train 데이터 read
train.columns = ['TIME','EAST','WEST','SOUTH','NORTH','ABS','OUTPUT','MODE']    #columns 지정

test = pd.read_csv('test.csv')     #test 데이터 read
test.columns = ['TIME','EAST','WEST','SOUTH','NORTH','ABS','OUTPUT','MODE']    #columns 지정

print("\n 1.TRAIN DATA\n")
print(train.head())    #train데이터 확인
print("\n 2.TEST DATA\n")
print(test.head())  #test데이터 확인

#TIME column은 DecisionTreeClassifier 라이브러리로 사용하는데 에러사항이 있어 빼고학습
train_X = train[['EAST','WEST','SOUTH','NORTH','ABS','OUTPUT']].values    #train 입력 데이터
train_y = train['MODE'].values   #train 출력 데이터

test_X = test[['EAST','WEST','SOUTH','NORTH','ABS','OUTPUT']].values    #test 입력 데이터
test_y = test['MODE'].values   #test 출력 데이터

tree = DecisionTreeClassifier(max_depth=2) #깊이를 4~7정도로 높였을때 오히려 정확도가 떨어짐
tree.fit(train_X,train_y)       #학습진행

#테스트 데이터에대한 정확도 측정

pred_train = tree.predict(train_X)    #train_x 데이터를 사용하여 예측
pred_test = tree.predict(test_X)    #test_X 데이터를 사용하여 예측

print(type(pred_test))  #예측데이터 타입확인 numpy.ndarray
print(type(test_y)) #test_y 타입확인 numpy.ndarray

print("학습데이터에 대한 정확도:",metrics.accuracy_score(train_y,pred_train)) #성능측정 test_y와 pred_test를 비교하여 성능을 측정한다.
print("테스트데이터에 대한 정확도:",metrics.accuracy_score(test_y,pred_test)) #성능측정 test_y와 pred_test를 비교하여 성능을 측정한다.

plt.figure()            #결정트리 시각화
plot_tree(tree,filled=True)
plt.show()