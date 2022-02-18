#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

#define INF (1 << 30)
int N, M;
string disables;

bool canTurn(string channel) {
	for(int i=0; i<disables.size(); ++i) {
		char disable = disables[i];	
		auto it = find(channel.begin(), channel.end(), disable);
		if(it != channel.end())
			return false;
	}
	return true;
}

int solve() {
	int ret = abs(N-100);
	for(int i=0; i<=1e6; ++i) {
		string channel = to_string(i);
		if(canTurn(channel)) {
			ret = min(ret, (int)channel.size() + abs(N-i));
		}
	}
	return ret;
}

int main() {
	cin >> N >> M;
	for(int i=0; i<M; ++i) {
		string button;	
		cin >> button;
		disables += button;
	}
	cout << solve();
	return 0;
}
