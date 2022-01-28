#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

const int INF = 2e9;

int N;
int dp[100001];

int dfs(int num) {
	if(num == 0)
		return 0;
	int &ret = dp[num];
	if(ret != -1)
		return ret;
	ret = INF;
	for(int i=1; i*i<=num; ++i)
		ret = min(ret, dfs(num - i*i) + 1);
	return ret;	
}

int main() {
	cin >> N;
	memset(dp, -1, sizeof(dp));
	cout << dfs(N);
	return 0;
}
