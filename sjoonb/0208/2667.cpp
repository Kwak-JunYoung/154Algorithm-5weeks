#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N;
vector<vector<int> > houses;
vector<vector<bool> > isVisited;

const int dy[4] = {-1, 0, 1, 0};
const int dx[4] = {0, 1, 0, -1};

bool inRange(int y, int x) {
	if(y >= 0 && y < N && x >= 0 && x < N)
		return true;
	return false;
}

int dfs(int y, int x) {
	isVisited[y][x] = true;
	int ret = 1;
	for(int k=0; k<4; ++k) {
		int ny = y + dy[k];
		int nx = x + dx[k];
		if(inRange(ny, nx) && !isVisited[ny][nx] && houses[ny][nx])
			ret += dfs(ny, nx);
	}
	return ret;
}

void solve() {
	vector<int> ret;
	for(int i=0; i<N; ++i)
		for(int j=0; j<N; ++j)
			if(!isVisited[i][j] && houses[i][j])
				ret.push_back(dfs(i, j));
	cout << ret.size() << "\n";
	sort(ret.begin(), ret.end());
	for(int i=0; i<ret.size(); ++i)
		cout << ret[i] << "\n";
}

int main() {
	cin >> N;
	houses = vector<vector<int> >(N, vector<int>(N, 0));
	isVisited = vector<vector<bool> >(N, vector<bool>(N, false));
	for(int i=0; i<N; ++i) {
		string row;
		cin >> row;
		for(int j=0; j<row.size(); ++j)
			if(row[j] == '1')
				houses[i][j] = 1;
	}
	solve();
	return 0;	
}

