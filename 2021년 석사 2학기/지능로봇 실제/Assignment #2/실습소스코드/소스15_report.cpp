#include <iostream>

using namespace std;

/* Rectangle �����*/
class Rectangle {
public:
    int width;  ///width�� height �ΰ��� ������ �ʿ�
    int height;
    double getArea();   ///����� ���� �Լ�
};

/* Rectangle ������*/
double Rectangle::getArea() {
    return width * height;  ///������ width�� height�� ���Ѱ�
}

int main() {
    Rectangle rect;     ///��ü����
    rect.width = 3;     ///rect�� ��� ���� ���� width = 3
    rect.height = 5;    ///rect�� ��� ���� ���� height = 5
    cout << "�簢���� ������" << rect.getArea() << endl;   ///rect�� ��� �Լ� ȣ�� �� ���
}
