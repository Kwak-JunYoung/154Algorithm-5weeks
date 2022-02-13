#include <iostream>
#include <vector>
using namespace std;

int N;
vector<vector<int> > board;

bool check(int y, int x, int size, int type) {
	for(int i=y; i<y+size; ++i)
		for(int j=x; j<x+size; ++j) 
			if(board[i][j] != type)
				return false;
	return true;
}


void div(int y, int x, int size) {
	int type = board[y][x];	
	if(check(y, x, size, type)) {
		cout << type;
		return;
	}
	int nextSize = size/2;
	cout << "(";
	for(int i=0; i<2; ++i)
		for(int j=0; j<2; ++j)
			div(y + i*nextSize, x + j*nextSize, nextSize);
	cout << ")";
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cin >> N;
	board = vector<vector<int> >(N, vector<int>(N));
	for(int i=0; i<N; ++i) {
		string row;	
		cin >> row;
		for(int j=0; j<row.size(); ++j) 
			board[i][j] = row[j] - '0';
	}
	div(0, 0, N);
	return 0;	
}
