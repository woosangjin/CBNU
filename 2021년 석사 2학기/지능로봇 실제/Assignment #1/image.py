# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 18:58:47 2021

@author: WSJ
"""

import matplotlib.pyplot as plt #그래프 모듈 임포트
from matplotlib.image import imread #이미지 모듈 임포트

img = imread('wsj.jpg')     #이미지 파일 read

#이미지표시
plt.imshow(img) 
plt.show()
