#include <iostream>
#include <algorithm>
#include <unordered_set>
#include <queue>
using namespace std;

#define ll long long
#define INF (1<<30)

ll dest;

const int dy[4] = {-1, 0, 1, 0};
const int dx[4] = {0, 1, 0, -1};

unordered_set<ll> visited;

struct element {
	int y, x, cnt;
	ll state;	
};

int get(ll mask, int index) {
	return (mask >> (index << 2)) & 15;
}

ll set(ll mask, int index, ll value) {
	return (mask & ~(15LL << (index << 2))) | (value << (index << 2));
}

void print(ll state) {
	cout << "\n";
	for(int i=0; i<3; ++i) {
		for(int j=0; j<3; ++j)
			cout << get(state, i*3 + j) << " ";
		cout << "\n";
	}
}

ll swap(int cy, int cx, int ny, int nx, ll state) {
	ll cval = get(state, cy * 3 + cx);
	ll nval = get(state, ny * 3 + nx);
	state = set(state, cy * 3 + cx, nval);
	state = set(state, ny * 3 + nx, cval);
	return state;
}

bool inRange(int y, int x) {
	if(x >= 0 && x < 3 && y >= 0 && y < 3)
		return true;
	return false;
}


bool isVisited(ll state) {
	auto it = visited.find(state);
	return (it != visited.end()) ? true : false;
}

int bfs(int y, int x, ll state) {
	queue<element> q;
	element start = { y, x, 0, state };
	visited.insert(start.state);
	q.push(start);
	while(!q.empty()) {
		element here = q.front();
		q.pop();	
		if(here.state == dest)
			return here.cnt;
		for(int k=0; k<4; ++k) {
			int ny = here.y + dy[k];		
			int nx = here.x + dx[k];		
			if(inRange(ny, nx)) {
				ll nextState = swap(here.y, here.x, ny, nx, here.state);
				if(!isVisited(nextState)) {
					visited.insert(nextState);	
					element there = { ny, nx, here.cnt + 1, nextState };
					q.push(there);
				}
			}
		}
	}
	return -1;
}

int main() {
	for(int i=1; i<=8; ++i) {
		dest = set(dest, i-1, i);
	}
	ll mask = 0;
	int y, x;
	for(int i=0; i<3; ++i)
		for(int j=0; j<3; ++j) {
			int val;
			cin >> val;
			mask = set(mask, i*3 + j, val);
			if(val == 0) {
				y = i;		
				x = j;
			}
		}
	visited.insert(mask);
	cout << bfs(y, x, mask);
	return 0;
}
