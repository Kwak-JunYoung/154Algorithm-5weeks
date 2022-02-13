#include <iostream>
#include <vector>
using namespace std;

int N;
int ret[3];
vector<vector<int> > paper;


void solve(int y, int x, int w) {
	int type = paper[y][x];
	bool isSame = true;
	for(int i=y; i<y+w; ++i) {
		if(!isSame)
			break;
		for(int j=x; j<x+w; ++j)
			if(type != paper[i][j])  {
				isSame = false;
				break;
			}
	}
	if(isSame) {
		ret[type+1]++;
	} else {
		int nw = w/3;
		for(int i=0; i<3; ++i)
			for(int j=0; j<3; ++j)
				solve(y + i*nw, x + j*nw, nw);
	}
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cin >> N;
	paper = vector<vector<int> >(N, vector<int>(N));
	for(int i=0; i<N; ++i)
		for(int j=0; j<N; ++j)
			cin >> paper[i][j];
	solve(0, 0, N);
	for(int i=0; i<3; ++i)
		cout << ret[i] << "\n";
	return 0;
}
