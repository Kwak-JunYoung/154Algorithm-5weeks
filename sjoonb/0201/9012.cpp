#include <iostream>
#include <stack>
using namespace std;

string str;

bool isCorrect() {
	stack<int> stk;
	for(int i=0; i<str.size(); ++i) {
		int bracket = str[i];	
		if(bracket == '(') {
			stk.push(bracket);
		} else {
			if(stk.empty())
				return false;
			stk.pop();
		}
	}
	return stk.empty() ? true : false;	
}

int main() {
	int cases;
	cin >> cases;
	for(int cc=0; cc<cases; ++cc) {
		cin >> str;
		isCorrect() ? cout << "YES" : cout << "NO";
		cout << "\n";
	}
	return 0;
}
