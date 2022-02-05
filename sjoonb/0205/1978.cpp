#include <iostream>
#include <cstring>
using namespace std;

int N;
bool isPrime[1001];

void eratosthenes() {		
	memset(isPrime, true, sizeof(isPrime));
	isPrime[1] = false;
	for(int i=2; i*i<=1000; ++i) {
		if(isPrime[i])	
			for(int j=i*2; j<=1000; j+=i)
				isPrime[j] = false;
	}
}

int main() {
	eratosthenes();
	cin >> N;	
	int ret = 0;
	for(int i=0; i<N; ++i) {
		int num;
		cin >> num;
		if(isPrime[num])
			ret++;
	}
	cout << ret;
	return 0;
}
