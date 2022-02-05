#include <iostream>
using namespace std;

int N;

void solve() {
	int i = 2;
	while(N != 1) {
		while(N % i == 0) {
			cout << i << "\n";
			N /= i;	
		}
		i++;
	}
}

int main() {	
	//cin >> N;
	N = 1e7-1;
	solve();
	return 0;
}
