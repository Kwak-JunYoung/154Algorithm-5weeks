#include <iostream>
#include <vector>
#include <cstring>
using namespace std;

int N;
bool isVisited[100001];
bool inCurrentCycle[100001];

vector<int> graph;
vector<int> notInTeam;

void dfs(int here) {
	notInTeam.push_back(here);
	isVisited[here] = true;
	inCurrentCycle[here] = true;
	int there = graph[here];
	if(inCurrentCycle[there]) {
		while(notInTeam.back() != there)
			notInTeam.pop_back();
		notInTeam.pop_back();
	} else if(!isVisited[there]) {
		dfs(there);
	}
	inCurrentCycle[here] = false;
}

int solve() {
	memset(isVisited, false, sizeof(isVisited));
	notInTeam = vector<int>();
	for(int i=1; i<=N; ++i) {
		if(!isVisited[i]) {
			dfs(i);
		}
	}
	return notInTeam.size();
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);
	int cases;
	cin >> cases;
	for(int cc=0; cc<cases; ++cc) {
		cin >> N;
		graph = vector<int>(N+1);
		for(int i=1; i<=N; ++i)
			cin >> graph[i];
		cout << solve() << "\n";
	}
	return 0;
}


