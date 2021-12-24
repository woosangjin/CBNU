# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 20:52:23 2021

@author: WSJ
"""

from matplotlib import pyplot as plt #그래프 모듈 임포트
from matplotlib.image import imread #이미지 모듈 임포트

img = imread('wsj.jpg')     #이미지 파일 read

#이미지표시
# R:G:B cmap = 색상 vmin,vmax= 비선형 확장변수 interpolation = 보간법
plt.imshow(img[:,:,1], cmap='gray', vmin = 0, vmax = 255,interpolation='none') 
plt.show()

#R,G 밝은 색을제거