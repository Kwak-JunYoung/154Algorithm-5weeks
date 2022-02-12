#include <iostream>
#include <set>
using namespace std;

int N, M;
set<int> bst;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cin >> N;
	for(int i=0; i<N; ++i) {
		int num;
		cin >> num;
		bst.insert(num);
	}
	cin >> M;
	for(int i=0; i<M; ++i) {
		int num;
		cin >> num;	
		set<int>::iterator it = bst.find(num);
		cout << (it != bst.end() ? 1 : 0) << " ";
	}
	return 0;
}
