#include <iostream>
#include <cstring>
#include <queue>
using namespace std;

bool isPrime[10000];
int dist[10000];

void eratosthenes() {
	memset(isPrime, true, sizeof(isPrime));
	isPrime[1] = false;
	for(int i=2; i*i<=1e4; ++i)
		if(isPrime[i])
			for(int j=i*2; j<=1e4; j+=i)
				isPrime[j] = false;
}

bool inRange(int x) {
	if(x >= 1e3 && x < 1e4)
		return true;
	return false;
}

int bfs(int start, int dest) {
	queue<int> q;
	q.push(start);
	dist[start] = 0;
	while(!q.empty()) {
		int here = q.front();	
		q.pop();
		if(here == dest)
			return dist[here];
		for(int i=0; i<4; ++i) {
			string pwd = to_string(here);
			for(int j=0; j<10; ++j) {
				string cand = string(1, (char) j + '0');
				pwd.replace(i, 1, cand);	
				int there = stoi(pwd);
				if(inRange(there) && dist[there] == -1 && isPrime[there]) {
					q.push(there);
					dist[there] = dist[here]+1;
				}
			}
		}
	}
	return -1;	
}

int main() {
	eratosthenes();
	int cases;
	cin >> cases;
	for(int cc=0; cc<cases; ++cc) {
		int A, B;
		cin >> A >> B;
		memset(dist, -1, sizeof(dist));
		int ret = bfs(A, B);
		if(ret != -1)
			cout << ret;
		else
			cout << "Impossible";
		cout << "\n";
	}
	return 0;
}
