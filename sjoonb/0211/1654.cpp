#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N, M;
vector<int> tree;

long long f(int x) {
	long long ret = 0;
	for(int i=0; i<N; ++i) 
		ret += max(0, tree[i] - x);
	return ret;
}

int bisection(int lo, int hi) {
	for(int i=0; i<100; ++i) {
		int mid = (lo + hi) / 2;	
		long long fmid = f(mid);
		if(fmid < M)
			hi = mid;
		else
			lo = mid;
	}
	return (lo + hi) / 2;
}

int main() {
	cin >> N >> M;
	tree = vector<int>(N);
	for(int i=0; i<N; ++i)
		cin >> tree[i];
	cout << bisection(0, 1e9+1);
	return 0;	
}
