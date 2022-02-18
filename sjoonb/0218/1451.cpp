#include <iostream>
#include <algorithm>
using namespace std;

int N, M;
long long sum[51][51];

long long solve() {
	long long ret = -1;
	for(int i=1; i<=N; ++i)
		for(int j=1; j<=M; ++j)
			sum[i][j] = sum[i-1][j] + sum[i][j-1] + sum[i][j] - sum[i-1][j-1];
	for(int i=1; i<N; ++i)
		for(int j=1; j<M; ++j) {
			ret = max(ret, sum[i][j] * (sum[N][j] - sum[i][j]) * (sum[N][M] - sum[N][j]));
			ret = max(ret, sum[N][j] * (sum[i][M] - sum[i][j]) * (sum[N][M] - sum[N][j] - sum[i][M] + sum[i][j]));
			ret = max(ret, sum[i][M] * (sum[N][j] - sum[i][j]) * (sum[N][M] - sum[N][j] - sum[i][M] + sum[i][j]));
			ret = max(ret, sum[i][j] * (sum[i][M] - sum[i][j]) * (sum[N][M] - sum[i][M]));
		}
	for(int i=1; i<M-1; ++i)
		for(int j=i+1; j<M; ++j)
			ret = max(ret, sum[N][i] * (sum[N][j] - sum[N][i]) * (sum[N][M] - sum[N][j]));
	for(int i=1; i<N-1; ++i)
		for(int j=i+1; j<N; ++j)
			ret = max(ret, sum[i][M] * (sum[j][M] - sum[i][M]) * (sum[N][M] - sum[j][M]));
	return ret;
}

int main() {
	cin >> N >> M;
	for(int i=1; i<=N; ++i) {
		string str;
		cin >> str;
		for(int j=1; j<=M; ++j)
			sum[i][j] = str[j-1] - '0';
	}
	cout << solve();
	return 0;
}
