#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

int N;
int board[2][100000];
int dp[3][100000];

//		  cols

// type 0 o 
//		  x

// type 1 x 
//		  o

// type 2 x 
//		  x

int dfs(int type, int cols) {
	if(cols == N)
		return 0;
	int &ret = dp[type][cols];
	if(ret != -1)
		return ret;
	ret = 0;
	if(type == 2)
		for(int type=0; type<3; ++type)
			ret = max(ret, dfs(type, cols+1));
	else
		for(int k=1; k<=2; ++k)
			ret = max(ret, dfs((type+k)%3, cols+1) + board[type][cols]);
		
	return ret;
}

int main() {
	int cases;
	cin >> cases;
	for(int cc=0; cc<cases; ++cc) {
		memset(dp, -1, sizeof(dp));
		cin >> N;
		for(int i=0; i<2; ++i)
			for(int j=0; j<N; ++j)
				cin >> board[i][j];
		int ret = 0;
		for(int type=0; type<3; ++type)
			ret = max(ret, dfs(type, 0));
		cout << ret << endl;
	}

	return 0;	
}

