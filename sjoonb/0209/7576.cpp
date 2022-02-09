#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int W, H;
int nTomato;
int matures;
vector<vector<int> > tomatos;
vector<vector<int> > days;
queue<pair<int, int> > q;

const int dy[4] = {-1, 0, 1, 0};
const int dx[4] = {0, 1, 0, -1};

bool inRange(int y, int x) {
	if(y >= 0 && y < H && x >= 0 && x < W)
		return true;
	return false;
}

int bfs() {
	int ret = 0;
	while(!q.empty()) {
		pair<int, int> here = q.front();
		int cy = here.first;
		int cx = here.second;
		q.pop();
		for(int k=0; k<4; ++k) {
			int ny = cy + dy[k];	
			int nx = cx + dx[k];	
			if(inRange(ny, nx) && tomatos[ny][nx] == 0) {
				q.push(make_pair(ny, nx));
				tomatos[ny][nx] = 1;
				matures++;
				int cand = days[ny][nx] = days[cy][cx] + 1;
				ret = max(ret, cand);
			}
		}
	}
	return (nTomato == matures) ? ret : -1;
}

int main() {
	cin >> W >> H;
	tomatos = vector<vector<int> >(H, vector<int>(W));
	days = vector<vector<int> >(H, vector<int>(W, 0));
	nTomato = H*W;
	matures = 0;
	for(int i=0; i<H; ++i)
		for(int j=0; j<W; ++j) {
			int tomato;
			cin >> tomato;
			if(tomato == -1) {
				nTomato--;
			} else if(tomato == 1) {
				q.push(make_pair(i, j));
				matures++;
			}
			tomatos[i][j] = tomato;
		}
	cout << bfs();
	return 0;	
}
