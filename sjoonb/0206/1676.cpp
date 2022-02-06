#include <iostream>
using namespace std;

const long long MOD = 1e16;
int N;

int solve() {
	int cnt = 0;
	long long val = 1;
	for(long long i=2; i<=N; ++i) {
		val *= i;	
		while(val % 10 == 0) {
			cnt++;
			val /= 10;
		}
		val %= MOD;
	}
	return cnt;
}

int main() {
	//cin >> N;	
	for(int i=0; i<=500; ++i) {
		N = i;
		cout << "#" << i << ": " << solve() << "\n";
	}
	return 0;
}
