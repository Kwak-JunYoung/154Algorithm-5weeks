#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;

string str;

int convert(string bin) {
	int ret = 0;
	int square = 0;
	for(int i=bin.size()-1; i>=0; --i)	
		ret += (bin[i] - '0') * pow(2, square++);
	return ret;
}

void solve() {
	int r = str.size() % 3;

	if(r != 0)
		cout << convert(str.substr(0, r));

	for(int i=r; i<str.size(); i+=3)
		cout << convert(str.substr(i, 3));
				
}

int main() {
	cin >> str;	
	solve();	
	return 0;
}
