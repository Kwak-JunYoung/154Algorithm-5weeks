#include <iostream>
#include <vector>
using namespace std;

int N;
vector<pair<int, int> > ret;

void hanoi(int src, int dest, int n) {
	if(n < 1)
		return;
	hanoi(src, 3 - (src + dest), n-1); 	
	ret.push_back(make_pair(src, dest));
	hanoi(3 - (src + dest), dest, n-1); 	
}

int main() {
	cin >> N;
	hanoi(0, 2, N);
	cout << ret.size() << "\n";
	for(int i=0; i<ret.size(); ++i)
		printf("%d %d\n", ret[i].first+1, ret[i].second+1);
	return 0;	
}
