#include <iostream>
#include <cstring>
using namespace std;

int N;
int graph[1001];
bool isVisited[1001];

bool isCycle(int here) {
	isVisited[here] = true;
	if(isVisited[graph[here]])
	return isVisited = isCycle(graph[here]);
}

int solve() {
	memset(isVisited, false, sizeof(isVisited));
	int ret = 0;	
	for(int i=1; i<=N; ++i) {
		if(!isVisited[i] && isCycle(i))
			ret++;
	}
	return ret;
}

int main() {
	int cases;
	cin >> cases;
	for(int cc=0; cc<cases; ++cc) {
		cin >> N;	
		for(int u=1; u<=N; ++u) {
			int v;
			cin >> v;
			graph[u] = v;
		}
		cout << solve() << "\n";
	}
	return 0;
}
