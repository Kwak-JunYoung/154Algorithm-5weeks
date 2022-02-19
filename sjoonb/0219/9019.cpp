#include <iostream>
#include <queue>
#include <cstring>
#include <algorithm>
using namespace std;

int parent[10001];
char op[10001];

void D(int here, queue<int> &q) {
	int there = (here * 2) % (int)1e4;
	if(parent[there] != -1)
		return;
	parent[there] = here;
	op[there] = 'D';
	q.push(there);
}

void S(int here, queue<int> &q) {
	int there = here - 1;
	if(there < 0)
		there = 9999;
	if(parent[there] != -1)
		return;
	parent[there] = here;
	op[there] = 'S';
	q.push(there);
}

void L(int here, queue<int> &q) {
	int there = (here % 1000) * 10 + (here / 1000);
	if(parent[there] != -1)
		return;
	parent[there] = here;
	op[there] = 'L';
	q.push(there);
}

void R(int here, queue<int> &q) {
	int there = (here % 10) * 1000 + (here / 10);
	if(parent[there] != -1)
		return;
	parent[there] = here;
	op[there] = 'R';
	q.push(there);
}

void bfs(int start, int dest) {
	queue<int> q;
	q.push(start);
	parent[start] = start;
	while(!q.empty()) {
		int here = q.front();
		q.pop();
		if(here == dest)
			return;
		D(here, q);
		S(here, q);
		L(here, q);
		R(here, q);
	}
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	int cases;
	cin >> cases;
	for(int cc=0; cc<cases; ++cc) {
		int A, B;
		cin >> A >> B;
		memset(parent, -1, sizeof(parent));
		bfs(A, B);
		int here = B;
		string ret;
		while(parent[here] != here) {
			ret += op[here];
			here = parent[here];
		}
		reverse(ret.begin(), ret.end());
		cout << ret << "\n";
	}
	return 0;	
}
