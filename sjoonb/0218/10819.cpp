#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;

int N;
int seq[8];
bool isVisited[8];

int brf(int curr) {
	int ret = 0;
	for(int next=0; next<N; ++next) 
		if(!isVisited[next]) {
			isVisited[next] = true;
			ret = max(ret, brf(next) + abs(seq[curr] - seq[next]));	
			isVisited[next] = false;
		}
	return ret;	
}

int main() {
	cin >> N;
	for(int i=0; i<N; ++i)
		cin >> seq[i];
	int ret = 0;
	for(int src=0; src<N; ++src) {
		isVisited[src] = true;
		ret = max(ret, brf(src));
		isVisited[src] = false;
	}
	cout << ret;
	return 0;	
}
