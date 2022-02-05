#include <iostream>
using namespace std;

int gcd(long long a, long long b) {
	if(b == 0)
		return a;
	return gcd(b, a%b);
}

int main() {
	long long a, b;	
	cin >> a >> b;
	int n = gcd(a, b);
	for(int i=0; i<n; ++i)
		cout << 1;
	return 0;
}
