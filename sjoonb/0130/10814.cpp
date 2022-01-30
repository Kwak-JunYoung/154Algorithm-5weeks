#include <iostream>
#include <algorithm>
using namespace std;

int N;
pair<int, string> members[100000];

bool cmp(pair<int,string> a, pair<int,string> b)
{
    return a.first < b.first;
}

int main() {
	cin >> N;
	for(int i=0; i<N; ++i) {
		int age;
		string name;	
		cin >> age >> name;
		members[i] = make_pair(age, name);
	}
	stable_sort(members, members+N, cmp);
	for(int i=0; i<N; ++i)
		cout << members[i].first << " " << members[i].second << "\n";
	return 0;
}
