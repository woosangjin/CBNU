# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 08:42:54 2021

@author: WSJ
"""

import matplotlib.pyplot as plt #그래프 모듈 임포트
import math #수학공식 모듈 임포트

class Graph:    #Graph 클래스생성

    def sin(self):  #sin메소드
        for x in range(0,360,5):            #0~360까지 반복 5씩증가
            y = math.sin(math.pi * x/180)   #sin값 계산
            plt.subplot(221)                #그래프를 각각 표시하기위한 좌표지정
            plt.title("sin")                #차트 제목 설정
            plt.plot(x,y, 'ro')             #그래프 생성
    
    def cos(self):  #cos메소드
        for x2 in range(0,360,5):            #0~360까지 반복 5씩증가
            y2 = math.cos(math.pi * x2/180)  #cos값 계산
            plt.subplot(222)                 #그래프를 각각 표시하기위한 좌표지정
            plt.title("cos")                 #차트 제목 설정
            plt.plot(x2,y2, 'ro')            #그래프 생성    

    def tan(self):  #tan메소드
        for x3 in range(0,360,5):            #0~360까지 반복 5씩증가 
            y3 = math.tan(math.pi * x3/180)  #tan값 계산 
            plt.subplot(223)                 #그래프를 각각 표시하기위한 좌표지정
            plt.title("tan")                 #차트 제목 설정
            plt.plot(x3,y3, 'ro')            #그래프 생성    

    def log(self):  #log메소드
        for x4 in range(1,360,1):            #1~360까지 반복 1씩증가
            y4 = math.log(math.pi * x4/180)  #log값 계산
            plt.subplot(224)                 #그래프를 각각 표시하기위한 좌표지정
            plt.title("log")                 #차트 제목 설정
            plt.plot(x4,y4, 'ro')            #그래프 생성  

plt.subplots_adjust(hspace=1)                #그래프 겹침방지

# sin그래프
p1=Graph()
p1.sin()

# cos그래프
p2=Graph()
p2.cos()

# tan그래프
p3=Graph()
p3.tan()

# log그래프
p1=Graph()
p1.log()

plt.legend()    #범례 표시
plt.show()      #그래프 표출