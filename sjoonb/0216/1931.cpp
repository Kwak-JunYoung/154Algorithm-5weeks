#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N;
vector<pair<int, int> > meetings;


int solve() {
	sort(meetings.begin(), meetings.end());
	int begin = meetings[0].first;
	int end = meetings[0].second;
	int ret = 1;
	for(int i=1; i<N; ++i) {
		pair<int, int> meeting = meetings[i];	
		if(meeting.first >= end) {
			begin = meeting.first;
			end = meeting.second;
			ret += 1;		
		} else if(meeting.second < end) {
			end = meeting.second;	
		}
	}
	return ret;
}

int main() {
	cin >> N;
	meetings = vector<pair<int, int> >(N);
	for(int i=0; i<N; ++i) {
		int start, end;
		cin >> start >> end;
		meetings[i] = make_pair(start, end);
	}
	cout << solve();
	return 0;
}
