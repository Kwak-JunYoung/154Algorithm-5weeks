#include <iostream>
#include <cstring>
using namespace std;

const int SIZE = 1e6;

int M, N;
bool isPrime[SIZE+1];

void eratosthenes() {		
	memset(isPrime, true, sizeof(isPrime));
	isPrime[1] = false;
	for(int i=2; i*i<=SIZE; ++i) {
		if(isPrime[i])	
			for(int j=i*2; j<=SIZE; j+=i)
				isPrime[j] = false;
	}
}

int main() {
	ios::sync_with_stdio(false);
	cout.tie(NULL);
	cin.tie(NULL);
	eratosthenes();
	cin >> M >> N;	
	for(int i=M; i<=N; ++i) {
		if(isPrime[i])
			cout << i << "\n";
	}
	return 0;
}
