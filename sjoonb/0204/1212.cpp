#include <iostream>
using namespace std;

string str;

string convert(int num) {
	string ret = "";
	int i = 4;
	while(i >= 1) {
		ret += (num/i + '0');	
		num %= i;
		i /= 2;	
	}
	return ret;
}

void solve() {
	string ret = "";
	for(int i=0; i<str.size(); ++i) {
		ret += convert(str[i] - '0');
	}
	int idx=0;
	while(ret[idx] == '0' && idx < ret.size()-1) {
		idx++;
	}
	for(int i=idx; i<ret.size(); ++i)
		cout << ret[i];
}

int main() {
	cin >> str;	
	solve();
	return 0;
}
