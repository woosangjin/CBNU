#include <iostream>

using namespace std;

int main() {
    int n[10]; //���� 10��¥�� �� �޸� ����
    double d[] = { 0.1,0.2,0.5,3.9 }; //�迭d�� 0.1,0.2,0.5,3.9�� �ʱ�ȭ

    int i;
    for (i = 0; i < 10; i++) n[i] = i * 2; //2�� ����� n�� ���� ä��
    for (i = 0; i < 10; i++) cout << n[i] << ' ';//�迭n���
    cout << "\n"; //�� �� �ڴ�.

    double sum = 0; // c++������ �ʿ��Ҷ� ������ �ƹ� ���̳� ���� ����
    for (i = 0; i < 4; i++) {//�迭d�� �� ���
        sum += d[i];
    }

    cout << "�迭 d������ " << sum;//�迭d�� �� ���
}
