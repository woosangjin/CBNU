#include <iostream>

using namespace std;

/* Circle �����*/
///�Ʒ� �ҽ��ڵ忡�� ����ο� �����Լ��� ����
class Circle {
    int radius;
public:
    Circle() { radius = 1; }
    Circle(int radius) { this->radius = radius; }
    void setRadius(int radius) { this->radius = radius; }   ///������ ���� �Լ�
    double getArea() { return 3.14 * radius * radius; }     ///����� ���� �Լ�
};

/*readRadius �Լ�����*/
///Ű����� ������ �Է¹޾� radius�� ���� ����
void readRadius(Circle& read) {
    int a;  ///�������� ����
    cin >> a;   ///�������� a�� �Է°� ����
    read.setRadius(a);
}

int main() {
    Circle donut;   ///��ü ����
    readRadius(donut);  ///�Լ� ȣ��
    cout << "donut�� ���� = " << donut.getArea() << endl;  ///donut�� ��� �Լ� ȣ�� �� ���
}

