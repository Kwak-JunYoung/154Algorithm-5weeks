#include <iostream>
#include <cstring>
using namespace std;

int N;
int dp[10][1000];

const int MOD = 1e4 + 7;

int dfs(int src, int depth) {
	if(depth == N)
		return 1;
	int &ret = dp[src][depth];
	if(ret != -1)
		return ret;
	ret = 0;
	for(int next=src; next<10; ++next) {
		ret = (ret + dfs(next, depth+1)) % MOD;
	}
	return ret %= MOD;
}

int main() {
	memset(dp, -1, sizeof(dp));
	cin >> N;	
	cout << dfs(0, 0);
}
