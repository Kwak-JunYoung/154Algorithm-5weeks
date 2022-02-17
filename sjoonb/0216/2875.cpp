#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

int N, M, intern;

int main() {
	cin >> N >> M >> intern;
	int team = min(N/2, M);
	int remain = (N - team * 2) + (M - team);
	if(remain >= intern) {
		cout << team;
	} else {
		team -= ceil((intern - remain) / 3.0);
		cout << team;
	}
}
