#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int A, P;
bool isVisited[3000001];
vector<int> graph;

int dfs(int here) {
	isVisited[here] = true;
	graph.push_back(here);
	int there = 0;
	while(here > 0) {
		int digit = here % 10;
		there += pow(digit, P);	
		here /= 10;	
	}
	if(!isVisited[there])
		return dfs(there);
	return there;
}

int solve() {
	int repition = dfs(A);	
	vector<int>::iterator it = find(graph.begin(), graph.end(), repition);
	graph = vector<int>(graph.begin(), it);
	return graph.size();	
}

int main() {
	cin >> A >> P;
	cout << solve();
}


