#include <iostream>
#include <vector>
using namespace std;

int N, M;
vector<vector<int> > graph;
vector<bool> isVisited;

void dfs(int here) {
	isVisited[here] = true;	
	for(int i=0; i<graph[here].size(); ++i) {
		int next = graph[here][i];
		if(!isVisited[next])
			dfs(next);
	}
}

int main() {
	cin >> N >> M;
	graph = vector<vector<int> >(N+1, vector<int>(N+1));
	isVisited = vector<bool>(N+1, false);
	for(int i=0; i<M; ++i) {
		int u, v;
		cin >> u >> v;
		graph[u].push_back(v);
		graph[v].push_back(u);
	}
	int cnt=0;
	for(int i=1; i<=N; ++i) {
		if(!isVisited[i]) {
			dfs(i);
			cnt++;
		}
	}
	cout << cnt;
	return 0;	
}
