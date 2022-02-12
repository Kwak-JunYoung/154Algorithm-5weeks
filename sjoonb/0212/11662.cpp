#include <iostream>
#include <cmath>
using namespace std;

double Ax, Ay, Bx, By, Cx, Cy, Dx, Dy;

double f(double rate) {
	double x1 = Ax + (Bx - Ax) * rate;
	double y1 = Ay + (By - Ay) * rate;
	double x2 = Cx + (Dx - Cx) * rate;
	double y2 = Cy + (Dy - Cy) * rate;
	return sqrt(pow(x2 - x1, 2) + pow(y2-y1,2));
}

double ternary(double lo, double hi) {
	for(int i=0; i<100; ++i) {
		double a = (2*lo + hi) / 3.0;
		double b = (lo + 2*hi) / 3.0;
		if(f(a) > f(b))
			lo = a;
		else
			hi = b;
	}
	return (lo + hi) / 2.0;
}

int main() {	
	cout << fixed;
	cout.precision(6);
	cin >> Ax >> Ay;
	cin >> Bx >> By;
	cin >> Cx >> Cy;
	cin >> Dx >> Dy;
	double rate = ternary(0.0, 1.0);
	cout << f(rate);
	return 0;
}
