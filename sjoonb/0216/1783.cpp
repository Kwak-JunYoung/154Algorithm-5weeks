#include <iostream>
using namespace std;

int N, M;

int solve() {
	if(N == 1) {
		return 1;	
	} else if(N == 2) {
		return min(3, (M+1) / 2);
	} else if(N >= 3) {
		if(M <= 6)
			return min(M, 4);
		else
			return 5 + (M - 7);
	}
	return -1;
}

int main() {
	cin >> N >> M;
	cout << solve();
	return 0;
}
