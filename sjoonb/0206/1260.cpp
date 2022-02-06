#include <iostream>
#include <cstring>
#include <vector>
#include <queue>
using namespace std;

int N, M, V;
vector<vector<bool> > adjM;


bool isVisited[1001];

void dfs(int src) {
	isVisited[src] = true;
	cout << src << " ";
	for(int next=1; next<=N; ++next) {
		if(adjM[src][next] && !isVisited[next]) {
			dfs(next);
		}
	}
}

void bfs(int src) {
	queue<int> q;	
	q.push(src);
	isVisited[src] = true;
	while(!q.empty()) {
		int here = q.front();
		q.pop();
		cout << here << " ";
		for(int next=1; next<=N; ++next) {
			if(adjM[here][next] && !isVisited[next]) {
				q.push(next);
				isVisited[next] = true;
			}
		}
	}
}

int main() {
	cin >> N >> M >> V;
	adjM = vector<vector<bool> >(N+1, vector<bool>(N+1));
	for(int i=0; i<M; ++i) {
		int u, v;
		cin >> u >> v;
		adjM[u][v] = true;
		adjM[v][u] = true;
	}
	dfs(V);
	cout << "\n";
	memset(isVisited, false, sizeof(isVisited));
	bfs(V);
	return 0;
}

