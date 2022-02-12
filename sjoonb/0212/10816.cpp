#include <iostream>
#include <map>
using namespace std;

int N, M;
map<int, int> bst;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cin >> N;
	for(int i=0; i<N; ++i) {
		int num;
		cin >> num;
		auto it = bst.find(num);
		if(it != bst.end())
			it->second++;
		else
			bst.insert(make_pair(num, 1));
	}
	cin >> M;
	for(int i=0; i<M; ++i) {
		int num;
		cin >> num;
		auto it = bst.find(num);
		if(it != bst.end())
			cout << it->second;
		else
			cout << 0;
		cout << " ";
	}
	return 0;
}
