#include <iostream>
#include <set>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

#define x first
#define y second
#define INF (1<<30)


int N;
vector<pair<int, int> > points;
set<pair<int, int> > bst;

int dist(const pair<int, int> &a, const pair<int, int> &b) {
	return pow(b.x - a.x, 2) + pow(b.y - a.y, 2);
}

int solve() {
	int minDist = dist(points[1], points[0]);
	bst.emplace(points[0].y, points[0].x);
	bst.emplace(points[1].y, points[1].x);
	int j=0;
	for(int i=2; i<N; ++i) {
		while(j < i && pow(points[i].x - points[j].x, 2) >= minDist) {
			bst.erase({points[j].y, points[j].x});
			j += 1;
		}
		auto begin = bst.lower_bound(make_pair(points[i].y - sqrt(minDist), -INF));
		auto end = bst.upper_bound(make_pair(points[i].y + sqrt(minDist), INF));
		for(auto it = begin; it != end; it++)
			minDist = min(minDist, dist(points[i], {it->second, it->first}));
		bst.emplace(points[i].y, points[i].x);
	}
	return minDist;	
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cin >> N;
	for(int i=0; i<N; ++i) {
		int x, y;
		cin >> x >> y;
		points.emplace_back(x, y);
	}
	sort(points.begin(), points.end());
	cout << solve();
	return 0;
}

