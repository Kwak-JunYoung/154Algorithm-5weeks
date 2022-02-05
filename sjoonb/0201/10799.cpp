#include <iostream>
#include <stack>
using namespace std;

string str;

int solve() {
	int ret = 0;
	int stack = 0;
	for(int i=0; i<str.size(); ++i) {
		if(i+1 < str.size() && str[i] == '(' && str[i+1] == ')') {
			ret += stack; 
			i+=1;
		} else if(str[i] == '(') {
			ret += 1;
			stack += 1;
		} else {
			stack -= 1;
			
		}
	}
	return ret;	
}

int main() {
	cin >> str;
	cout << solve();
	return 0;	
}


