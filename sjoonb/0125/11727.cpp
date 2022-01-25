#include <iostream>
#include <cstring>
using namespace std;

int N;
int dp[1000];

int dfs(int i) {
	if(i >= N)
		return (i == N) ? 1 : 0;
	int &ret = dp[i];
	if(ret != -1) {
		return ret;
	}
	ret = 0;
	ret += dfs(i+1);
	ret += 2*dfs(i+2);
	return ret %= 10007;
}

int main() {
	cin >> N;
	memset(dp, -1, sizeof(dp));
	cout << dfs(0);	
	return 0;
}
