#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

int N;
int V[10000];
int dp[3][10000];

int dfs(int cnt, int i) {
	if(i == N)
		return 0;	
	int &ret = dp[cnt][i];
	if(ret != -1)
		return ret;
	ret = dfs(0, i+1); 
	if(cnt+1 < 3)
		ret = max(ret, dfs(cnt+1, i+1) + V[i]);
	return ret;
}

int main() {
	memset(dp, -1, sizeof(dp));
	cin >> N;
	for(int i=0; i<N; ++i)
		cin >> V[i];
	cout << dfs(0, 0);
}

