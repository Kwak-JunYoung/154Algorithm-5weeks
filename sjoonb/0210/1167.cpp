#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
using namespace std;

int V;
bool isVisited[100001];
int child[100001];
vector<vector<pair<int, int> > > graph;

int dfs(int here) {
	isVisited[here] = true;
	int ret = 0;
	for(int i=0; i<graph[here].size(); ++i) {
		int there = graph[here][i].first;
		int dist = graph[here][i].second;
		if(!isVisited[there]) {
			int cand = dfs(there) + dist;
			if(ret < cand) {
				ret = cand;
				child[here] = there;
			}
		}
	}
	return ret;
}

int solve() {
	int node = 1;
	dfs(node);
	while(child[node] != 0) {
		node = child[node];
	}
	memset(isVisited, false,  sizeof(isVisited));
	int ret = dfs(node);
	return ret;
}

int main() {
	cin >> V;
	graph = vector<vector<pair<int, int> > >(V+1);
	for(int i=0; i<V; ++i) {
		int u, v, w;	
		cin >> u;
		while(true) {
			cin >> v;	
			if(v == -1)
				break;
			cin >> w;
			graph[u].push_back(make_pair(v, w));
		}
	}
	cout << solve();
	return 0;	
}
