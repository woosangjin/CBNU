#include <iostream>

using namespace std;

int main() {
    int n = 10, m;
    char c = 'A';
    double d;

    int* p = &n; //p��n�� �ּҰ��� ����
    char* q = &c; //q��c�� �ּҰ��� ����
    double* r = &d; //r�� d�� �ּҰ��� ����

    *p = 25; //n�� 25�� �����
    *q = 'A';//C�� ����'A'�� �����
    *r = 3.14;//d�� 3.14�� �����
    m = *p + 10; //p�� ����Ű�� ��(n ������)+10�� m�� ����

    cout << n << ' ' << *p << "\n"; //�Ѵ� 25�� ��µ�
    cout << c << ' ' << *q << "\n"; //�Ѵ� 'A'�� ��µ�
    cout << d << ' ' << *r << "\n"; //�Ѵ�3.14�� ��µ�
    cout << m << "\n"; //m�� 35���
}