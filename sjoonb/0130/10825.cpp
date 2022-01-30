#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

int N;

#define KOR 1
#define ENG 2
#define MATH 3

typedef tuple<string, int, int, int> grade;
grade seq[100000];

bool cmp(const grade &a, const grade &b)
{
	if(get<KOR>(a) == get<KOR>(b) && get<ENG>(a) == get<ENG>(b) && get<MATH>(a) == get<MATH>(b)) 
		return get<0>(a) < get<0>(b);

	else if(get<KOR>(a) == get<KOR>(b) && get<ENG>(a) == get<ENG>(b))
		return get<MATH>(a) > get<MATH>(b);

	else if(get<KOR>(a) == get<KOR>(b))
		return get<ENG>(a) < get<ENG>(b);

	else
		return get<KOR>(a) > get<KOR>(b);
}

int main() {
	cin >> N;
	for(int i=0; i<N; ++i) {
		string str;
		int a, b, c;
		cin >> str >> a >> b >> c;
		seq[i] = make_tuple(str, a, b, c);
	}
	sort(seq, seq+N, cmp);
	for(int i=0; i<N; ++i) {
		cout << get<0>(seq[i]) << "\n";
	}
   	return 0;
}
