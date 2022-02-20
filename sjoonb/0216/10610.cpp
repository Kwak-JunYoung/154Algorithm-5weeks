#include <iostream>
#include <algorithm>
using namespace std;

string numbers;

string solve() {
	int sum = 0;
	bool isZeroExist = false;
	for(int i=0; i<numbers.size(); ++i) {
		int number = numbers[i] - '0';
		sum += number;	
		if(!isZeroExist && number == 0)
			isZeroExist = true;
	}
	if(sum % 3 == 0 && isZeroExist) {
		sort(numbers.begin(), numbers.end(), greater<int>());
		return numbers;
	} else {
		return "-1";
	}
}

int main() {
	cin >> numbers;
	cout << solve();
}
