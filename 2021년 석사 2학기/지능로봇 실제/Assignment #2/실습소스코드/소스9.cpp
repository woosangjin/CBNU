#include <iostream>

using namespace std;

int main() {
    int n = 10, m;
    char c = 'A';
    double d;

    int* p = &n; //p는n의 주소값을 가짐
    char* q = &c; //q는c의 주소값을 가짐
    double* r = &d; //r은 d의 주소값을 가짐

    *p = 25; //n에 25가 저장됨
    *q = 'A';//C에 문자'A'가 저장됨
    *r = 3.14;//d에 3.14가 저장됨
    m = *p + 10; //p가 가리키는 값(n 변수값)+10을 m에 저장

    cout << n << ' ' << *p << "\n"; //둘다 25가 출력됨
    cout << c << ' ' << *q << "\n"; //둘다 'A'가 출력됨
    cout << d << ' ' << *r << "\n"; //둘다3.14가 출력됨
    cout << m << "\n"; //m값 35출력
}