#include <iostream>

using namespace std;

int main() {
    int n[10];
    int i;
    int* p;

    for (i = 0; i < 10; i++)
        *(n + i) = i * 3; //배열의 이름n을 주소처럼 사용 가능.배열n을 3의 배수로 채움

    p = n; //포인터 p에 배열n의 시작 주소를 설정한다.
    for (i = 0; i < 10; i++) {
        cout << *(p + i) << ' ';//포인터 p를 이용하여 배열n의 원소 접근
    }
    cout << "\n";

    for (i = 0; i < 10; i++) {
        *p = *p + 2; //포인터p를 이용하여 배열의 원소 값을 2증가
        p++; //p는 다음 원소의 주소로 증가
    }

    for (i = 0; i < 10; i++)
        cout << n[i] << ' ';
    cout << "\n";
}