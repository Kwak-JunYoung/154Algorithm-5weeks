#include <iostream>
#include <vector>
using namespace std;


string convert(int N, int B) {
	vector<int> vec;
	while(N > 0) {
		vec.push_back(N % B);
		N /= B;
	}
	string ret;
	for(int i=vec.size()-1; i>=0; --i) {
		ret.push_back(vec[i] < 10 ? '0' + vec[i] : 'A' + vec[i] - 10);
	}
	return ret;
}

int main() {
	int N, B;
	cin >> N >> B;
	cout << convert(N, B);
	return 0;
}
