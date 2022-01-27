#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

enum Order { normal, reverse };

int N;
int seq[1000];
int dp[2][1002][1000];

int dfs(int num, int i, Order order) {
	if(order == Order::normal && i == N || order == Order::reverse && i == -1)
		return 0;
	

	int &ret = dp[order][num][i];
	if(ret != -1)
		return ret;

	switch(order) {
		case Order::normal:
			ret = dfs(num, i+1, order);
			if(seq[i] < num)
				ret = max(ret, dfs(seq[i], i+1, order) + 1);
			break;

		case Order::reverse:
			ret = dfs(num, i-1, order);
			if(seq[i] < num)
				ret = max(ret, dfs(seq[i], i-1, order) + 1);
			break;
	}

	return ret;
}

int main() {
	memset(dp, -1, sizeof(dp));
	cin >> N;
	for(int i=0; i<N; ++i)
		cin >> seq[i];

	int a = dfs(1001, 0, Order::normal);
	int b = dfs(1001, N-1, Order::reverse);

	int ret = 0;
	for(int i=0; i<N; ++i) {
		ret = max(ret, dp[Order::normal][1001][i] + dp[Order::reverse][1001][i] - 1);
	}
	cout << ret;

	return 0;
}
