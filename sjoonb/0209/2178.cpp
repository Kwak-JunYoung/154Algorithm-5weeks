#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int N, M;

bool maze[100][100];
bool isVisited[100][100];
int parent[100][100];

const int dy[4] = {-1, 0, 1, 0};
const int dx[4] = {0, 1, 0, -1};

bool inRange(int y, int x) {
	if(y >= 0 && y < N && x >=0 && x < M)
		return true;
	return false;
}

int bfs() {
	queue<pair<int, int> > q;
	q.push(make_pair(0, 0));
	parent[0][0] = 1;
	isVisited[0][0] = true;
	while(!q.empty()) {
		pair<int, int> here = q.front();	
		q.pop();
		int cy = here.first;
		int cx = here.second;
		for(int k=0; k<4; ++k) {
			int ny = cy + dy[k];	
			int nx = cx + dx[k];	
			if(inRange(ny, nx) && !isVisited[ny][nx] && maze[ny][nx]) {
				parent[ny][nx] = parent[cy][cx] + 1;
				if(ny == N-1 && nx == M-1)
					return parent[ny][nx];
				isVisited[ny][nx] = true;	
				q.push(make_pair(ny, nx));
			}
		}
	}
	return 0;
}

int main() {
	cin >> N >> M;	
	for(int i=0; i<N; ++i) {
		string str;
		cin >> str;
		for(int j=0; j<str.size(); ++j)
			maze[i][j] = str[j] - '0';
	}
	cout << bfs();
	return 0;
}

