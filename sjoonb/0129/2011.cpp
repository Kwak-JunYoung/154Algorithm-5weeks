#include <iostream>
#include <cstring>
using namespace std;

const int MOD = 1e6;

int N;
int pw[5000];
int dp[5000];

int dfs(int i) {
	if(i == N)
		return 1;
	if(pw[i] == 0)
		return 0;

	int &ret = dp[i];
	if(ret != -1)
		return ret;	

	ret = dfs(i+1);
	
//	if(i+2 <= N && pw[i] >= 1 && pw[i] <= 2 && pw[i+1] >= 0 && pw[i+1] <=6)  // in this case, can't consider 17, 18, 19
	if(i+2 <= N) {
		int sum = pw[i] * 10 + pw[i+1];
		if(sum >= 10 && sum <= 26)
			ret = (ret + dfs(i+2)) % MOD;
	}

	return ret %= MOD;
}

int main() {
	memset(dp, -1, sizeof(dp));
	string str;
	cin >> str;
	N = str.size();
	for(int i=0; i<N; ++i)
		pw[i] = str[i] - '0';
	cout << dfs(0);
	return 0;
}
