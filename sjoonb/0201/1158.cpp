#include <iostream>
#include <queue>
using namespace std;

int N, K;
queue<int> q;

int main() {
	cin >> N >> K;	
	for(int i=1; i<=N; ++i)
		q.push(i);
	cout << "<";
	int cnt = 1;
	while(!q.empty()) {
		int curr = q.front();
		q.pop();
		if(cnt++ % K != 0)
			q.push(curr);
		else {
			cout << curr;
			if(!q.empty())
				cout << ", ";
		}
	}
	cout << ">";
	return 0;
}
