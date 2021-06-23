# 라이브러리 import
import os #디렉토리 설정을 위한 라이브러리
from selenium import webdriver #webdriver를 제어하기위한 라이브러리
from urllib.parse import quote_plus #아스키코드로 인코딩하기위한 라이브러리
import time #시간관련 처리를 위한 라이브러리
import urllib.request #url을 가져오기 위한 라이브러리


options = webdriver.ChromeOptions() # chromedirver 연동

driver = webdriver.Chrome("./chromedriver") #크롬드라이버 경로설정
driver.maximize_window() #웹사이즈 최대창 크기로 설정

baseUrl = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query=" #네이버주소 검색어만 바꿀수있도록분리
plusUrl = input("검색어 입력 : ") #검색어 입력

url = baseUrl + quote_plus(plusUrl) #전체 url 완성

driver.get(url) #이미지가 있는 url에 접근

assert "네이버" in driver.title #검색엔진으로 네이버를 사용하기때문에 중간점검용도

prev_height = driver.execute_script("return document.scrollHeight") #스크롤 깊이 측정

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)") #스크롤 끝까지 내리기

    time.sleep(1)   #딜레이 함수 1초

    curr_height = driver.execute_script("return document.body.scrollHeight") #스크롤 깊이 재측정
    if(curr_height == prev_height) :    #스크롤이 끝까지 내려간다면 break로 탈출, 아니라면 prev_height 갱신후 스크롤 내리기
        try:
            break
        except:
            break
    prev_height = curr_height

images = driver.find_elements_by_css_selector("._image")    #css 선택자 조건을 만족하는 모든 요소를 리스트에 담아 반환

imgDirpath = "./img"
keywordDirpath = "./img/" + plusUrl

if len(images) > 0: #images에 데이터가 저장되었는지 판별
    if not os.path.exists(imgDirpath):  #img데이터 유무를 판단
        os.makedirs(imgDirpath)     #img 폴더생성

Cnt = 1
for image in images :
    try:
        imgUrl = image.get_attribute("src") #src획득 요소의 이름

        opener=urllib.request.build_opener() #각각의 이미지 경로에 해당그림리소스를 요청
        opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')] #브라우저의 버전등을 명시
        urllib.request.install_opener(opener) #이미지 다운로드
        urllib.request.urlretrieve(imgUrl, "./img/" + "/" + str(Cnt) + ".jpg") #img폴더에 jpg형태로저장

        Cnt = Cnt + 1
    except:
        pass

driver.close()  #브라우저 닫기

