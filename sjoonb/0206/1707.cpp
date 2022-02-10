#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int V, E;
vector<vector<int> > graph;
vector<int> colors;

bool isBipartite(int src) {
	queue<int> q;
	q.push(src);
	colors[src] = 0;
	while(!q.empty()) {
		int here = q.front();	
		q.pop();
		for(int i=0; i<graph[here].size(); ++i) {
			int there = graph[here][i];	
			if(colors[there] == -1)  {
				colors[there] = (colors[here] + 1) % 2;
				q.push(there);
			}
			else if(colors[there] == colors[here])
				return false;
		}
	}
	return true;
}

void solve() {
	for(int i=1; i<=V; ++i) {
		if(colors[i] == -1)
			if(!isBipartite(i)) {
				cout << "NO\n";
				return;
			}
	}
	cout << "YES\n";
}

int main() {
	int cases;
	cin >> cases;
	for(int cc=0; cc<cases; ++cc) {
		cin >> V >> E;	
		graph = vector<vector<int> >(V+1);
		colors = vector<int>(V+1, -1);
		for(int i=0; i<E; ++i) {
			int u, v;
			cin >> u >> v;
			graph[u].push_back(v);
			graph[v].push_back(u);
		}
		solve();
	}
	return 0;	
}

