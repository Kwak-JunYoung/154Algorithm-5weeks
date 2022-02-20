#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int N;
vector<int> P;

int solve() {
	int ret = 0;
	int accumSum = 0;
	for(int i=0; i<N; ++i) {
		accumSum += P[i];	
		ret += accumSum;
	}
	return ret;
}

int main() {
	cin >> N;
	P = vector<int>(N);
	for(int i=0; i<N; ++i)
		cin >> P[i];
	sort(P.begin(), P.end());
	cout << solve();
	return 0;
}
