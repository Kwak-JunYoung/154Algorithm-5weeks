#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int N;

void solve() {
	if(N==0) {
		cout << 0;
		return;
	}

	vector<int> res;
	while(N != 0) {
		res.push_back(abs(N % -2));
		N = ceil((double)N / -2.0);
	}
	for(int i=res.size()-1; i>=0; --i)
		cout << res[i];
}

int main() {
	cin >> N;	
	solve();
}
