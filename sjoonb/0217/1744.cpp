#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int N;
int zeroCnt;
int oneCnt;
vector<int> negSeq;
vector<int> posSeq;

int main() {
	cin >> N;
	for(int i=0; i<N; ++i) {
		int num;
		cin >> num;
		if(num > 1)
			posSeq.push_back(num);
		else if(num < 0)
			negSeq.push_back(num);
		else
			if(num == 0)
				zeroCnt++;
			else if(num == 1)
				oneCnt++;
	}
	sort(posSeq.begin(), posSeq.end(), greater<int>());
	sort(negSeq.begin(), negSeq.end());
	int ret = oneCnt;
	for(int i=1; i<posSeq.size(); i+=2) 
		ret += posSeq[i-1] * posSeq[i];	
	if(posSeq.size() % 2 == 1)
		ret += posSeq[posSeq.size()-1];
	for(int i=1; i<negSeq.size(); i+=2)
		ret += negSeq[i-1] * negSeq[i];	
	if(negSeq.size() % 2 == 1 && zeroCnt == 0)
		ret += negSeq[negSeq.size()-1];
	cout << ret;
	return 0;	
}
