#include <iostream>
#include <cstring>
using namespace std;

const int SIZE = 1e6;
bool isPrime[SIZE+1];

void eratosthenes() {
	memset(isPrime, true, sizeof(isPrime));
	for(int i=0; i<2; ++i)
		isPrime[i] = false;
	for(int i=2; i*i<=SIZE; ++i)
		if(isPrime[i])
			for(int j=i*2; j<=SIZE; j+=i)
				isPrime[j] = false;
}

void solve(int num) {
	for(int i=3; i<=SIZE/2; i+=2)
		if(isPrime[i] && isPrime[num-i]) {
			cout << num << " = " << i << " + " << (num-i) << "\n";
			return;
		}
	cout << "Goldbach's conjecture is wrong.\n";
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	eratosthenes();
	int input;
	cin >> input;
	while(input != 0) {
		solve(input);	
		cin >> input;
	}
	return 0;	
}
