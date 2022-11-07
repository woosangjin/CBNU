# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 22:54:01 2021

@author: wsj
"""

#아래 프로그램을 테스트하는 이유는 tensorflow 와 numpy가 호환되는것을 보이기 위해서 이다.(텐서플로 버전2.0부터 호환가능)

#pip install tensorflow 텐서플로 라이브러리 다운로드 1회실행만 해주면 됨

import tensorflow as tf #temsorflow 라이브러리 import 하고 tf라고 지칭한다
import numpy as np  #numpy 라이브러리 import 하고 np라고 지칭한다 tf,np는 사용자가 별도로 지정할수있다.

t=tf.random.uniform([2,3],0,1)  # tf.Tensor형의 2x3 행렬 생성 매개변수는 0,1이므로 0~1사이의 난수 생성후 변수 t에대입
n=np.random.uniform(0,1,[2,3])  # ndarray형의 2x3 행렬 생성 매개변수는 0,1 이므로 0~1 사이의 난수 생성후 변수 n에대입

print("tensorflow로 생성한 텐서:\n",t,"\n") #t에 저장되어있는 tf.Tensor형의 객체 출력 데이터 타입은 float32
print("numpy로 생성한 ndarray:\n",n,"\n") #n에 저장되어있는 ndarray형의 객체 출력 데이터 타입은 float32

res=t+n #tf.Tensor 객체 + ndarray 객체를 더하여 res변수에 대입
print("덧셈결과:\n",res) #res변수 출력