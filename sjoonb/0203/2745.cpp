#include <iostream>
#include <cmath>
using namespace std;

string N;
int B;

int decode(char ch) {
	if(ch >= '0' && ch <= '9')
		return ch - '0';
	else if(ch >= 'A' && ch <= 'Z')
		return ch - 'A' + 10;
	return -1;
}

int convert() {
	int ret = 0;
	int square = 0;
	for(int i=N.size()-1; i>=0; --i) {
		int num = decode(N[i]);
		ret += num * pow(B, square++);
	}
	return ret;
}

int main() {
	cin >> N >> B;
	cout << convert();
	return 0;
}
