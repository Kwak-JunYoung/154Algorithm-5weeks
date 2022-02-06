#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

//long long dp[1001][1001];

int count(int num, int div) {
	int cnt = 0;
	for(long long i = div; i<=num; i*=div) {
		cnt += num / i;	
	}
	return cnt;	
}

//long long comb(int n, int r) {
//	if(n == 0 || n == r)
//		return 1;
//	if(r == 1)
//		return n;
//	long long &ret = dp[n][r];
//	if(ret != -1)
//		return ret;
//	return ret = (comb(n-1, r-1) + comb(n-1, r)) % (long long)1e17;
//}

int main() {
	int N, M;
	// for test
	//memset(dp, -1, sizeof(dp));
//	for(N=1; N<=1000; ++N)
//		for(M=0; M<=N; ++M)  {
//			int ret5 = count(N, 5) - (count(M, 5) + count(N-M, 5));
//			int ret2 = count(N, 2) - (count(M, 2) + count(N-M, 2));
//			int lv = min(ret5, ret2);
//
//			long long retComb = comb(N, M);
//			long long rv = 0;
//			while(retComb % 10 == 0) {
//				rv++;
//				retComb /= 10;
//			}
//			assert(lv == rv);
//		}
	cin >> N >> M;
	int ret5 = count(N, 5) - count(M, 5) - count(N-M, 5);
	int ret2 = count(N, 2) - count(M, 2) - count(N-M, 2);
	cout << min(ret5, ret2);
		
	return 0;
}
