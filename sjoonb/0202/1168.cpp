#include <iostream>
#include <vector>
using namespace std;

int N, K;
int tree[4 * (int)1e5];

int init(int start, int end, int node) {
	if(start == end) return tree[node] = 1;
	int mid = (start + end) / 2;
	return tree[node] = init(start, mid, node * 2) + init(mid+1, end, node * 2 + 1);
}

void update(int start, int end, int node, int index, int value) {
	if(index < start || index > end)
		return;
	tree[node] += value;
	if(start == end) return;
	int mid = (start + end) / 2;
	update(start, mid, node * 2, index, value);
	update(mid+1, end, node * 2 + 1, index, value);
}

int query(int start, int end, int node, int order) {
	if(start == end)
		return start;	
	int mid = (start + end) / 2;
	if(tree[node*2] >= order) return query(start, mid, node*2, order);
	else return query(mid+1, end, node*2 + 1, order - tree[node*2]);
}

int main() {
	cin >> N >> K;	
	init(0, N-1, 1);
	vector<int> orders;
	int order = 0;
	int size = N;
	for(int i=0; i<N; ++i) {
		order = (order + K - 1) % size;
		size--;
		orders.push_back(order+1);
	}
	cout << "<";
	for(int i=0; i<N; ++i) {
		int order = orders[i];
		int victim = query(0, N-1, 1, order);		
		update(0, N-1, 1, victim, -1);
		cout << victim+1;
		if(i != N-1)
			cout << ", ";
	}
	cout << ">";
	return 0;
}
