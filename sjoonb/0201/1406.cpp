#include <iostream>
#include <list>
using namespace std;

list<char> editor;
list<char>::iterator cursor;

void input(char cmd) {
	switch(cmd) {
		case 'B':
			if(cursor != editor.begin()) {
				list<char>::iterator tmp = cursor;
				editor.erase(--cursor);
				cursor = tmp;
			}
			break;
		case 'L':
			if(cursor != editor.begin())
				cursor--;
			break;
		case 'P':
			char ch;
			cin >> ch;
			editor.insert(cursor, ch);
			break;
		case 'D':
			if(cursor != editor.end())
				cursor++;
			break;
	}
}

int main() {
	string str;
	cin >> str;
	editor = list<char>(str.begin(), str.end());
	cursor = editor.end();
	int n;
	cin >> n;
	for(int i=0; i<n; ++i) {
		char cmd;
		cin >> cmd;
		input(cmd);
	}
	while(!editor.empty()) {
		cout << editor.front();
		editor.pop_front();
	}
}

