#include <iostream>
#include <cstring>
using namespace std;

const int MOD = 1e9;

int N, K;
int dp[200][201];

int dfs(int depth, int sum) {
	if(sum > 200)
		return 0;
	if(depth == K)
		return (sum == N) ? 1 : 0;
	int &ret = dp[depth][sum];
	if(ret != -1)
		return ret;
	ret = 0;
	for(int i=0; i<=N; ++i)
		ret = (ret + dfs(depth+1, sum+i)) % MOD;
	return ret;
}

int main() {
	memset(dp, -1, sizeof(dp));
	cin >> N >> K;
	cout << dfs(0, 0);
	return 0;
}
