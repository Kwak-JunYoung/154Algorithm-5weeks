#include <iostream>
#include <vector>
using namespace std;

int N, K;
int coins[10];

int solve() {
	int ret = 0;
	for(int i=N-1; i>=0; --i) {
		ret += K / coins[i];	
		K %= coins[i];
	}
	return ret;
}

int main() {
	cin >> N >> K;	
	for(int i=0; i<N; ++i)
		cin >> coins[i];
	cout << solve();
	return 0;
}
