#include <iostream>

using namespace std;

class Circle {
public:
    int radius;
    Circle(); // ¸Å°³ º¯¼ö ¾ø´Â »ý¼ºÀÚ
    Circle(int r); //¸Å°³ º¯¼ö ÀÖ´Â »ý¼ºÀÚ
    double getArea();
};

Circle::Circle() {
    radius = 1;
    cout << "¹ÝÁö¸§" << radius << "¿ø »ý¼º" << endl;
}

Circle::Circle(int r) {
    radius = r;
    cout << "¹ÝÁö¸§" << radius << "¿ø »ý¼º" << endl;
}

double Circle::getArea() {
    return 3.14 * radius * radius;
}

int main() {
    Circle donut; //¸Å°³ º¯¼ö ¾ø´Â »ý¼ºÀÚ È£­x
    double area = donut.getArea();
    cout << "donut ¸éÀûÀº" << area << endl;

    Circle pizza(30); //¸Å°³ º¯¼ö ÀÖ´Â »ý¼ºÀÚ È£Ãâ
    area = pizza.getArea();
    cout << "pizza ¸éÀûÀº " << area << endl;
}