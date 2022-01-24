#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

int N;
int dp[1000001];

int dfs(int num) {
	if(num == 1)
		return 0;
	int &ret = dp[num];
	if(ret != -1)
		return ret;
	ret = dfs(num-1) + 1;
	if(num%3 == 0)
		ret = min(ret, dfs(num/3) + 1);	
	if(num%2 == 0)
		ret = min(ret, dfs(num/2) + 1);	
	return ret;
}

int main() {
	cin >> N;
	memset(dp, -1, sizeof(dp));
	cout << dfs(N);	
}

