#include <iostream>
#include <algorithm>
#include <cstring>
#include <queue>
using namespace std;

int N;
bool map[100][100];
bool isVisited[100][100];
int dist[100][100];

const int dy[4] = {-1, 0, 1, 0};
const int dx[4] = {0, 1, 0, -1};

bool inRange(int y, int x) {
	if(y >= 0 && y < N && x >= 0 && x < N)
		return true;
	return false;	
}

void dfs(int y, int x) {
	isVisited[y][x] = true;		
	for(int k=0; k<4; ++k) {
		int ny = y + dy[k];
		int nx = x + dx[k];
		if(inRange(ny, nx) && !isVisited[ny][nx] && map[ny][nx])
			dfs(ny, nx);
	}
}

int bfs(int y, int x) {
	queue<pair<int, int> > q;	
	q.push(make_pair(y, x));
	isVisited[y][x] = true;
	bool oneSideConnected = false;
	int oneSideDist = 0;
	while(!q.empty()) {
		int cy = q.front().first;		
		int cx = q.front().second;		
		q.pop();
		for(int k=0; k<4; ++k) {
			int ny = cy + dy[k];	
			int nx = cx + dx[k];	
			if(inRange(ny, nx) && !isVisited[ny][nx]) {
				dist[ny][nx] = dist[cy][cx] + 1;
				if(map[ny][nx]) {
					if(!oneSideConnected) {
						oneSideConnected = true;
						oneSideDist = dist[ny][nx];
						dfs(ny, nx);
					} else {
						return oneSideDist + dist[ny][nx] - 1;	
					}
				}
				isVisited[ny][nx] = true;
				q.push(make_pair(ny, nx));
			}
		}
	}
	return 1e9;
}

int solve() {
	int ret = 1e9;
	for(int i=0; i<N; ++i)
		for(int j=0; j<N; ++j) 
			if(!map[i][j]) {
				memset(isVisited, false, sizeof(isVisited));
				memset(dist, 0, sizeof(dist));
				//cout << bfs(i, j) << "\n";
				ret = min(ret, bfs(i, j));
				
			}
	return ret;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);
	cin >> N;
	for(int i=0; i<N; ++i)
		for(int j=0; j<N; ++j)
			cin >> map[i][j];
	cout << solve();
	return 0;
}
