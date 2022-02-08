#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int W, H;
vector<vector<int> > islands;
vector<vector<bool> > isVisited;

const int dy[8] = {-1, -1, 0, 1, 1, 1, 0, -1};
const int dx[8] = {0, 1, 1, 1, 0, -1, -1, -1};

bool inRange(int y, int x) {
	if(y >= 0 && y < H && x >= 0 && x < W)
		return true;
	return false;
}

void dfs(int y, int x) {
	isVisited[y][x] = true;
	for(int k=0; k<8; ++k) {
		int ny = y + dy[k];
		int nx = x + dx[k];
		if(inRange(ny, nx) && !isVisited[ny][nx] && islands[ny][nx])
			dfs(ny, nx);
	}
}

int solve() {
	int ret = 0;
	for(int i=0; i<H; ++i)
		for(int j=0; j<W; ++j)
			if(!isVisited[i][j] && islands[i][j]) {
				dfs(i, j);
				ret++;
			}
	return ret;
}

int main() {
	while(true) {
		cin >> W >> H;
		if(H == 0 && W == 0)
			break;	
		islands = vector<vector<int> >(H, vector<int>(W, 0));
		isVisited = vector<vector<bool> >(H, vector<bool>(W, false));
		for(int i=0; i<H; ++i)
			for(int j=0; j<W; ++j)
				cin >> islands[i][j];
		cout << solve() << "\n";
	}
	return 0;	
}

