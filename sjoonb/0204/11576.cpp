#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

int A, B;
vector<int> numbers;

int A_to_decimal() {
	int ret = 0;
	for(int i=0; i<numbers.size(); ++i)
		ret += numbers[numbers.size() - i - 1] * pow(A, i);
	return ret;
}

vector<int> decimal_to_B(int num) {
	vector<int> ret;
	while(num > 0) {
		ret.push_back(num % B);
		num /= B;
	}
	reverse(ret.begin(), ret.end());
	return ret;
}

int main() {
	cin >> A >> B;
	int m;
	cin >> m;		
	numbers = vector<int>(m);
	for(int i=0; i<m; ++i)
		cin >> numbers[i];
	int decimal = A_to_decimal();
	vector<int> ret = decimal_to_B(decimal);
	for(int i=0; i<ret.size(); ++i)
		cout << ret[i] << " ";
	return 0;
}
