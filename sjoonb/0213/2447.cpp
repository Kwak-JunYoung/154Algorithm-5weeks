#include <iostream>
#include <vector>
using namespace std;

int N;
vector<string> output;

void div(int y, int x, int size) {
	if(size == 1) {
		output[y][x] = '*';
		return;
	}
	size /= 3;
	for(int i=0; i<3; ++i)
		for(int j=0; j<3; ++j)
			if(i != 1 | j != 1)
				div(y + i*size, x + j*size, size);
}

int main() {
	ios::sync_with_stdio(false);
	cin >> N;
	output = vector<string>(N, string(N, ' '));
	div(0, 0, N);
	for(int i=0; i<N; ++i)
		cout << output[i] << "\n";
	return 0;	
}
