#include <iostream>
using namespace std;

#define INF (1<<30)

int N;
int dest;
int dist[10][10];
bool isVisited[10];

int brf(int here, int depth) {
	if(depth == N)
		return (dist[here][0] > 0) ? dist[here][dest] : INF;
	int ret = INF;
	for(int there=0; there<N; ++there) {
		if(!isVisited[there] && dist[here][there] > 0) {
			isVisited[there] = true;
			ret = min(ret, brf(there, depth+1) + dist[here][there]);
			isVisited[there] = false;
		}
	}
	return ret;
}

int main() {
	cin >> N;
	for(int i=0; i<N; ++i)
		for(int j=0; j<N; ++j)
			cin >> dist[i][j];
	isVisited[0] = true;
	cout << brf(0, 1) << "\n";
	return 0;
}
