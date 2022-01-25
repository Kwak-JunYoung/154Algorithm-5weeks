#include <iostream>
#include <cstring>
using namespace std;

int N;
int dp[100][10];

int dfs(int depth, int num) {
	if(depth == N-1)
		return 1;
	int &ret = dp[depth][num];
	if(ret != -1)
		return ret;
	ret = 0;
	if(num + 1 < 10)
		ret += dfs(depth+1, num+1);
	if(num - 1 >= 0)
		ret += dfs(depth+1, num-1);
	return ret %= (int)1e9;
}

int solve() {
	int ret = 0;
	for(int i=1; i<10; ++i)	
		ret = (ret + dfs(0, i)) % (int)1e9;
	return ret;
}

int main() {
	cin >> N;
	memset(dp, -1, sizeof(dp));
	cout << solve();	
	return 0;
}

