# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 21:23:52 2021

@author: WSJ
"""

import numpy as np #numpy 배열 모듈 임포드
import matplotlib.pyplot as plt #그래프 모듈 임포트
from PIL import Image #이미지 모듈 임포트

image=Image.open('wsj.jpg')                 #이미지 파일 read
gray_image=image.convert('L')               #이미지 회색으로 변환
gray_image_array=np.asarray(gray_image)     #이미지를 NumPy배열로 변환   

#이미지표시  
plt.imshow(gray_image_array,cmap='gray', vmin = 0, vmax = 255)
plt.show()