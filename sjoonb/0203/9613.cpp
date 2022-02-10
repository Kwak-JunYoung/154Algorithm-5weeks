#include <iostream>
#include <vector>
using namespace std;

vector<int> vec;

int gcd(int a, int b) {
	if(b == 0)
		return a;
	return gcd(b, a%b);
}

long long solve() {
	long long ret = 0;	
	for(int i=0; i<vec.size()-1; ++i)
		for(int j=i+1; j<vec.size(); ++j)
			ret += gcd(vec[i], vec[j]);
	return ret;
}

int main() {
	int cases;
	cin >> cases;
	for(int cc=0; cc<cases; ++cc) {
		int n;
		cin >> n;	
		vec = vector<int>(n);
		for(int i=0; i<n; ++i)
			cin >> vec[i];
		cout << solve() << "\n";
	}
	return 0;
}
