#include <iostream>
#include <algorithm>
using namespace std;

int N;
pair<int, int> points[100000]; 

bool cmp(const pair<int, int> &a, const pair<int, int> &b) {
	if(a.second == b.second)
		return a.first < b.first;	
	return a.second < b.second;
}

int main() {
	cin >> N;
	for(int i=0; i<N; ++i) {
		int x, y;
		cin >> x >> y;
		points[i] = make_pair(x, y);
	}
	sort(points, points+N, cmp);
	for(int i=0; i<N; ++i)
		cout << points[i].first << " " << points[i].second << "\n";
	return 0;
}
