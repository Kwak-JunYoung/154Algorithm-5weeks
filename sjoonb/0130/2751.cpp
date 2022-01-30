#include <iostream>
#include <algorithm>
using namespace std;

int N;
int seq[1000000];

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cin >> N;
	for(int i=0; i<N; ++i)
		cin >> seq[i];
	sort(seq, seq + N);
	for(int i=0; i<N; ++i)
		cout << seq[i] << "\n";
	return 0;
}
