#include <iostream>
using namespace std;

int fact(int n) {
	int ret = 1;
	for(int i=1; i<=n; ++i)
		ret *= i;
	return ret;
}

int main() {
	int N;
	cin >> N;
	cout << fact(N);
	return 0;
}

