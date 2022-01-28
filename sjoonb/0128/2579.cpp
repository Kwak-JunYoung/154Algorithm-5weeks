#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

int N;
int stairs[301];
int dp[2][301];

int dfs(int cnt, int i) {
	if(i == N)
		return stairs[N];
	int &ret = dp[cnt][i];
	if(ret != -1)
		return ret;
	ret = 0;
	if(i+2 <= N)
		ret = max(ret, dfs(0, i+2) + stairs[i]);
	if(cnt+1 < 2)
		ret = max(ret, dfs(cnt+1, i+1) + stairs[i]);
	return ret;	
}

int main() {
	cin >> N;
	for(int i=1; i<=N; ++i)
		cin >> stairs[i];
	memset(dp, -1, sizeof(dp));
	int ret = dfs(0, 1);
	if(N >= 2)
		ret = max(ret, dfs(0, 2));
	cout << ret;
	return 0;
}
