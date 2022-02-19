#include <iostream>
#include <cstring>
#include <queue>
using namespace std;

int N, K;
int cnt[100001];

bool inRange(int x) {
	if(x >= 0 && x <= 1e5)
		return true;
	return false;
}

bool canVisit(int x) {
	return inRange(x) && cnt[x] == -1;
}

void visit(queue<int> &q, int here, int there) {
	q.push(there);	
	cnt[there] = cnt[here]+1;
}

int bfs(int src) {
	cnt[src] = 0;
	queue<int> q;
	q.push(src);
	while(!q.empty()) {
		int	here = q.front();
		q.pop();
		if(here == K)
			return cnt[here];
		if(canVisit(here-1))
			visit(q, here, here-1);
		if(canVisit(here+1))
			visit(q, here, here+1);
		if(canVisit(here*2))
			visit(q, here, here*2);
	}
	return 0;	
}

int main() {
	cin >> N >> K;
	memset(cnt, -1, sizeof(cnt));
	cout << bfs(N);
	return 0;	
}
