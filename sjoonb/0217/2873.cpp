#include <iostream>
using namespace std;

int R, C;
int posY, posX;
string ret;

void sol1() {
	ret += string(C-1, 'R');
	int repeat = (R-1)/2;
	for(int i=0; i<repeat; ++i) {
		ret += 'D';
		ret += string(C-1, 'L');
		ret += 'D';
		ret += string(C-1, 'R');
	}
}

void sol2() {
	ret += string(R-1, 'D');
	int repeat = (C-1)/2;
	for(int i=0; i<repeat; ++i) {
		ret += 'R';
		ret += string(R-1, 'U');
		ret += 'R';
		ret += string(R-1, 'D');
	}
}

void sol3() {
	int U = (posY % 2 == 1) ? posY-1 : posY;
	int L = (posX % 2 == 1) ? posX-1 : posX;
	int i, j;
	for(i=0; i<U; i+=2) {
		ret += string(C-1, 'R');	
		ret += 'D';
		ret += string(C-1, 'L');	
		ret += 'D';
	}
	for(j=0; j<L; j+=2) {
		ret += "DRUR";
	}
	if(posY % 2 == 1) {
		ret += "RD";	
	} else {
		ret += "DR";	
	}
	for(j = j+2; j<C; j+=2) {
		ret += "RURD";	
	}
	for(i= i+2; i<R; i+=2) {
		ret += 'D';
		ret += string(C-1, 'L');	
		ret += 'D';
		ret += string(C-1, 'R');	
	}
}

int main() {
	cin >> R >> C;
	int minNum = 1001;
	for(int i=0; i<R; ++i)
		for(int j=0; j<C; ++j) {
			int num;
			cin >> num;
			if((i + j) % 2 == 1 && num < minNum) {
				minNum = num;	
				posY = i;
				posX = j;
			}
		}
	if(R % 2 == 1) {
		sol1();
	} else if(C % 2 ==1) {
		sol2();
	} else {
		sol3();
	}
	cout << ret;
	return 0;	
}
