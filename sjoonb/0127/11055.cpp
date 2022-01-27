#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

int N;
int seq[1000];
int dp[1001][1000];

int dfs(int num, int i) {
	if(i == N)
		return 0;
	int &ret = dp[num][i];
	if(ret != -1)
		return ret;
	ret = dfs(num, i+1);
	if(seq[i] > num) 
		ret = max(ret, dfs(seq[i], i+1) + seq[i]);
	return ret;
}

int main() {
	memset(dp, -1, sizeof(dp));
	cin >> N;
	for(int i=0; i<N; ++i)
		cin >> seq[i];
	cout << dfs(0, 0);
	return 0;
}
