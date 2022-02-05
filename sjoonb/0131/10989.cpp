#include <iostream>
#include <algorithm>
using namespace std;

const int SIZE = 1e4 + 1;

int N;
int seq[SIZE];

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cin >> N;	
	for(int i=0; i<N; ++i) {
		int num;
		cin >> num;
		seq[num]++;
	}
	for(int i=0; i<SIZE; ++i) {
		for(int j=0; j<seq[i]; ++j)
			cout << i << "\n";
	}
	return 0;
}
