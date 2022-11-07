# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 23:40:38 2021

@author: wsj
"""
#pip install sklearn sklearn라이브러리 다운로드

from sklearn import datasets  #sklearn 라이브러리에서 datasets을 import한다
from sklearn.linear_model import Perceptron #sklearn.linear_model라이브러리에서 perceptron함수를 import한다.
from sklearn.model_selection import train_test_split  #sklearn.model_selection 라이브러리에서 train_test_split함수를 import 한다. (train데이터 test데이터 분할)
import numpy as np #numpy 라이브러리 import np로 명시

#데이터를 읽어와서 형식을 지정해주는 부분
digit=datasets.load_digits() #데이터셋에 저장되어있는 데이터를 digit변수에 저장
x_train,x_test,y_train,y_test=train_test_split(digit.data,digit.target,train_size=0.6)  #x학습 데이터,x테스트 데이터, y학습데이터,y테스트 데이터로 분할하여 각각 저장 훈련집합의 비율 0.6 테스트집합 비율 0.4
#교제에는 위에 구문이 두줄로 나와있는데 생각없이 줄바꿈하면 에러남

p=Perceptron(max_iter=100,eta0=0.001,verbose=0) #객체생성 :훈련데이터의수 100 학습률 0.001 학습중 데이터확인 안함 0:출력x,1:훈련진행사항출력
p.fit(x_train,y_train)  #fit함수는 학습함수로 x,y학습데이터로 학습한다

res=p.predict(x_test) #x테스트 데이터를 가지고 예측한 값을 res 변수에 저장한다.

conf=np.zeros((10,10))  #10x10 '0'으로 초기화된 배열생성하여 conf에 저장
for i in range(len(res)): #res 갯수만큼 반복
  conf[res[i]][y_test[i]]+=1  #행은 예측데이터 열은 y테스트데이터 판단에따라 각 위치에 1을 더한다.
print(conf) #conf변수에 저장되어있는 행렬 출력

no_correct=0  #정답 카운트를 위한 변수
for i in range(10): #10회 반복
  no_correct+=conf[i][i]  #정답인 경우 no_correct변수에 추가
accuracy=no_correct/len(res) #전체 데이터중 정답인 경우를 계산
print("테스트 집합에 대한 정확률은",accuracy*100,"%입니다.")  #정확률 출력