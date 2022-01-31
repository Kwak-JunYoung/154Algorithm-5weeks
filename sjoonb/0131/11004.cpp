#include <iostream>
#include <algorithm>
using namespace std;

const int SIZE = 5e6;

int N, K;
int seq[SIZE];

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cin >> N >> K;	
	for(int i=0; i<N; ++i)
		cin >> seq[i];
	sort(seq, seq+N);
	cout << seq[K-1];
	return 0;
}
