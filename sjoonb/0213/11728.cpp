#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N, M;
vector<int> A, B;

vector<int> merge() {
	int pa, pb;
	pa = pb = 0;
	vector<int> ret;
	while(pa < A.size() && pb < B.size()) {
		if(A[pa] < B[pb])	
			ret.push_back(A[pa++]);
		else
			ret.push_back(B[pb++]);
	}
	while(pa < A.size())
		ret.push_back(A[pa++]);
	while(pb < B.size())
		ret.push_back(B[pb++]);
	return ret;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cin >> N >> M;
	A = vector<int>(N);
	B = vector<int>(M);
	for(int i=0; i<N; ++i) {
		cin >> A[i];
	}
	for(int i=0; i<M; ++i) {
		cin >> B[i];
	}
	vector<int> ret = merge();	
	for(int i=0; i<ret.size(); ++i)
		cout << ret[i] << " ";
	return 0;
}

