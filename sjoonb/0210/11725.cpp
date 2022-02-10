#include <iostream>
#include <vector>
using namespace std;

int N;
int parents[100001];
bool isVisited[100001];
vector<vector<int> > graph;

void dfs(int here) {
	isVisited[here] = true;
	for(int i=0; i<graph[here].size(); ++i) {
		int there = graph[here][i];
		if(!isVisited[there]) {
			parents[there] = here;
			dfs(there);
		}
	}
}

void solve() {
	dfs(1);
	for(int i=2; i<=N; ++i)	{
		cout << parents[i] << "\n";	
	}
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);
	cin >> N;
	graph = vector<vector<int> >(N+1);
	for(int i=0; i<N-1; ++i) {
		int u, v;
		cin >> u >> v;
		graph[u].push_back(v);
		graph[v].push_back(u);
	}
	solve();
	return 0;	
}
