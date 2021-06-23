#영상 분류후 결과에 따라 해당 폴더에 저장하는 코드
import numpy as np
import tensorflow as tf
from PIL import Image
import os

cnn=tf.keras.models.load_model("my_cnn_cifar.h5") # 학습된 모델 불러오기
class_names=['apple', 'aquarium_fish', 'baby', 'bear', 'beaver', 'bed', 'bee', 'beetle', 'bicycle', 'bottle', 
             'bowl', 'boy', 'bridge', 'bus', 'butterfly', 'camel', 'can', 'castle', 'caterpillar', 'cattle', 
             'chair', 'chimpanzee', 'clock', 'cloud', 'cockroach', 'couch', 'crab', 'crocodile', 'cup', 'dinosaur', 
             'dolphin', 'elephant', 'flatfish', 'forest', 'fox', 'girl', 'hamster', 'house', 'kangaroo', 'keyboard', 
             'lamp', 'lawn_mower', 'leopard', 'lion', 'lizard', 'lobster', 'man', 'maple_tree', 'motorcycle', 'mountain', 
             'mouse', 'mushroom', 'oak_tree', 'orange', 'orchid', 'otter', 'palm_tree', 'pear', 'pickup_truck', 'pine_tree', 
             'plain', 'plate', 'poppy', 'porcupine', 'possum', 'rabbit', 'raccoon', 'ray', 'road', 'rocket', 
             'rose', 'sea', 'seal', 'shark', 'shrew', 'skunk', 'skyscraper', 'snail', 'snake', 'spider',
             'squirrel', 'streetcar', 'sunflower', 'sweet_pepper', 'table', 'tank', 'telephone', 'television', 'tiger', 'tractor',
             'train', 'trout', 'tulip', 'turtle', 'wardrobe', 'whale', 'willow_tree', 'wolf', 'woman', 'worm']

x_test=[]
img_orig=[]
fname=[]
for filename in os.listdir('./img'): # 폴더에서 테스트 영상 읽기
    if 'jpg' not in filename: # jpg 파일이 아닌 파일을 걸러내기
        continue
    img=Image.open('./img/'+filename) # jpg파일 open
    img_orig.append(img) # img_orig에 img추가
    fname.append(filename) # fname에 filename추가
    x=np.asarray(img.resize([32,32]))/255.0 # 32x32 크기조정, 0~1사이의 값으로 표준화
    x_test.append(x) # 영상 배열을 추가하는 구문
x_test=np.asarray(x_test) # ndarray형으로 형변환

pred=cnn.predict(x_test) # 예측

os.chdir('./img') # 디렉토리 지정
if not os.path.isdir('class_buckets'): # class_buckets 폴더 유무판단
    os.mkdir('class_buckets') # class_buckets 폴더생성
os.chdir('class_buckets') # 작업 디렉토리를 class_buckets로 변경

for i in range(len(class_names)): # 부류별로 폴더 만들기
    if not os.path.isdir(class_names[i]): # class이름으로 생성된 폴더가있는지 확인
        os.mkdir(class_names[i]) # class이름으로 폴더 생성

for i in range(len(x_test)): # 인식 결과에 따라 폴더에 저장
    folder_name=class_names[np.argmax(pred[i])] # 예측값 folder_name에 저장
    os.chdir(folder_name)   # 예측된 데이터로 디렉토리변경
    img_orig[i].save(fname[i])  # 예측된 데이터 저장
    os.chdir('..') #상위폴더로
    
