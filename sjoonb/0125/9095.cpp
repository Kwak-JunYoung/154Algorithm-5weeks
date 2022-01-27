#include <iostream>
#include <cstring>
using namespace std;

int N;
int dp[3][12];

int dfs(int num, int sum) {
	if(sum >= N)
		return (sum == N) ? 1 : 0;
	int &ret = dp[num-1][sum];
	if(ret != -1) 
		return ret;
	ret = 0;
	for(int i=1; i<=3; ++i)
		ret += dfs(i, sum+i);	
	return ret;
}

int main() {
	int cases;
	cin >> cases;
	for(int cc=0; cc<cases; ++cc) {
		cin >> N;
		memset(dp, -1, sizeof(dp));
		cout << dfs(1, 0) << endl;
	}
	return 0;
}
