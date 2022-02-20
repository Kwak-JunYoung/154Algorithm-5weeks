#include <iostream>
using namespace std;

int E, S, M;

bool isSame(int e, int s, int m) {
	if(e == E && s == S && m == M)
		return true;
	return false;
}

int solve() {
	int e, s, m, year;
	e = s = m = year = 1;
	while(!isSame(e, s, m)) {
		e = (e + 1 > 15) ? 1 : e+1;	
		s = (s + 1 > 28) ? 1 : s+1;	
		m = (m + 1 > 19) ? 1 : m+1;	
		year++;
	}
	return year;		
}

int main() {
	cin >> E >> S >> M;
	cout << solve();
	return 0;
}
