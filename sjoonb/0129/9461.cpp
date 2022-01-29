#include <iostream>
using namespace std;

long long dp[101];

void precalc() {
	dp[1] = 1;
	dp[2] = 1;
	dp[3] = 1;
	dp[4] = 2;
	dp[5] = 2;
	for(int i=6; i<=100; ++i)
		dp[i] = dp[i-1] + dp[i-5];
}

int main() {
	precalc();
	int cases;
	cin >> cases;
	for(int cc=0; cc<cases; ++cc) {
		int N;
		cin >> N;
		cout << dp[N] << endl;
	}
	return 0;
}
