#include <iostream>

using namespace std;

/* Circle 선언부*/
///아래 소스코드에는 선언부에 실제함수를 구현
class Circle {
    int radius;
public:
    Circle() { radius = 1; }
    Circle(int radius) { this->radius = radius; }
    void setRadius(int radius) { this->radius = radius; }   ///대입을 위한 함수
    double getArea() { return 3.14 * radius * radius; }     ///계산을 위한 함수
};

/*readRadius 함수구현*/
///키보드로 정수를 입력받아 radius에 값을 대입
void readRadius(Circle& read) {
    int a;  ///지역변수 생성
    cin >> a;   ///지역변수 a에 입력값 대입
    read.setRadius(a);
}

int main() {
    Circle donut;   ///객체 생성
    readRadius(donut);  ///함수 호출
    cout << "donut의 면적 = " << donut.getArea() << endl;  ///donut의 멤버 함수 호출 및 출력
}

