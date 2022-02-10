#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

string str;
vector<string> prefixes;

int main() {
	cin >> str;
	for(int i=0; i<str.size(); ++i) {
		prefixes.push_back(str.substr(i, str.size()));
	}
	sort(prefixes.begin(), prefixes.end());
	for(int i=0; i<prefixes.size(); ++i)
		cout << prefixes[i] << "\n";
	return 0;
}


