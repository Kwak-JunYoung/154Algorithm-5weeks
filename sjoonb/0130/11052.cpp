#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

int N;
int P[10001];
int dp[10001];

void solve() {
	for(int i=1; i<=N; ++i) {
		dp[i] = P[i];
		for(int j=1; j<=i/2; ++j)
			dp[i] = max(dp[i], dp[i-j] + dp[j]);
	}
}
	
int main() {
	memset(dp, -1, sizeof(dp));
	cin >> N;
	for(int i=1; i<=N; ++i)
		cin >> P[i];	
	solve();
	cout << dp[N];
	return 0;
}
