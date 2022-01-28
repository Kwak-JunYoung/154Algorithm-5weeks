#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

int N;
int seq[100000];
int dp[100000];

int solve() {
	int ret = -1001;
	int tempSum = 0;
	int j = 0;
	for(int i=0; i<N; ++i) {
		tempSum += seq[i];	
		ret = max(ret, tempSum);
		if(tempSum < 0) {
			tempSum = 0;	
		}
	}
	return ret;
}

int dfs(int i) {
	if(i == N)
		return 0;
	int &ret = dp[i];
	if(ret != -1)
		return ret;
	return ret = max(dfs(i+1) + seq[i], seq[i]);
}

int main() {
	memset(dp, -1, sizeof(dp));
	cin >> N;
	for(int i=0; i<N; ++i)
		cin >> seq[i];
	dfs(0);
	int ret = -1001;
	for(int i=0; i<N; ++i)
		ret = max(ret, dp[i]);
	cout << ret;
	return 0;
}
