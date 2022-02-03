#include <iostream>
using namespace std;

int gcd(int a, int b) {
	if(b == 0)
		return a;
	return gcd(b, a%b);
}

int lcm(int a, int b) {
	return a * b / gcd(a, b);
}

int main() {
	int cases;
	cin >> cases;
	for(int cc=0; cc<cases; ++cc) {
		int A, B;
		cin >> A >> B;
		cout << lcm(A, B) << "\n";
	}
	return 0;
}
