#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;

int N;
map<long long, int> M;
vector<pair<long long, int>> vec;

bool cmp(const pair<long long, int> &a, const pair<long long, int> &b) {
	if(a.second == b.second)
		return a.first < b.first;
	return a.second > b.second;
}

int main() {
	cin >> N;	
	for(int i=0; i<N; ++i) {
		long long num;
		cin >> num;
		map<long long, int>::iterator it = M.find(num);
		if(it == M.end())
			M.insert(make_pair(num, 0));
		else 
			it->second += 1;
	}
	map<long long, int>::iterator it;
	for(it = M.begin(); it != M.end(); it++) {
		vec.push_back(make_pair(it->first, it->second));	
	}
	sort(vec.begin(), vec.end(), cmp);
	cout << vec[0].first;
	return 0;
}
