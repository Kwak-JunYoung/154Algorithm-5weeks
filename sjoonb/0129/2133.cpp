#include <iostream>
#include <cstring>
using namespace std;

int N;
int dp[31];

int T(int n) {
	if(n <= 2)
		return (n == 2) ? 3 : 1;
	int &ret = dp[n];
	if(ret != -1)
		return ret;
	ret = 3*T(n-2);
	for(int i=4; i<=n; i+=2)
		ret += 2*T(n-i);
	return ret;
}
int main() {
	cin >> N;
	memset(dp, -1, sizeof(dp));
	if(N%2 == 1)
		cout << 0;
	else
		cout << T(N);
	return 0;	
}
