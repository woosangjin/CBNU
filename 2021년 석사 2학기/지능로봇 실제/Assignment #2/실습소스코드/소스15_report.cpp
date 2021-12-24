#include <iostream>

using namespace std;

/* Rectangle 선언부*/
class Rectangle {
public:
    int width;  ///width와 height 두개의 변수가 필요
    int height;
    double getArea();   ///계산을 위한 함수
};

/* Rectangle 구현부*/
double Rectangle::getArea() {
    return width * height;  ///면적은 width와 height를 곱한값
}

int main() {
    Rectangle rect;     ///객체생성
    rect.width = 3;     ///rect의 멤버 변수 접근 width = 3
    rect.height = 5;    ///rect의 멤버 변수 접근 height = 5
    cout << "사각형의 면적은" << rect.getArea() << endl;   ///rect의 멤버 함수 호출 및 출력
}
