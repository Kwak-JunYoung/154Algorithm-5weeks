#include <iostream>
#include <vector>
using namespace std;

int N;
vector<string> output;

void draw(int y, int x) {
	output[y][x+2] = '*';
	output[y+1][x+1] = '*';
	output[y+1][x+3] = '*';
	for(int i=0; i<5; ++i)
		output[y+2][x+i] = '*';
}

void div(int y, int x, int size) {
	if(size == 3) {
		draw(y, x);
		return;
	}
	int divSize = size / 2;
	div(y, x + divSize, divSize);
	div(y + divSize, x, divSize);
	div(y + divSize, x + divSize * 2 , divSize);
}

int main() {
	ios::sync_with_stdio(false);
	cin >> N;
	int M = (N * 2) - 1;
	output = vector<string>(N, string(M, ' '));
	div(0, 0, N);
	for(int i=0; i<N; ++i)
		cout << output[i] << "\n";
	return 0;	
}
