#include <iostream>
#include <vector>
#include <cstdlib>
using namespace std;

struct Node {
	char data;	
	Node* left;
	Node* right;
};

vector<Node> nodeList;

void preOrder(Node* node) {
	cout << node->data;
	if(node->left)
		preOrder(node->left);
	if(node->right)
		preOrder(node->right);
}

void inOrder(Node* node) {
	if(node->left)
		inOrder(node->left);
	cout << node->data;
	if(node->right)
		inOrder(node->right);
}

void postOrder(Node* node) {
	if(node->left)
		postOrder(node->left);
	if(node->right)
		postOrder(node->right);
	cout << node->data;
}

int main() {
	int N;
	cin >> N;
	for(int i=0; i<N; ++i) {
		Node node;
		node.data = 'A' + i;
		node.left = nullptr;
		node.right = nullptr;
		nodeList.push_back(node);
	}
	for(int i=0; i<N; ++i) {
		char root, left, right;	
		cin >> root >> left >> right;
		Node *node = &nodeList[root - 'A'];	

		if(left != '.')
			node->left = &nodeList[left - 'A'];

		if(right != '.')
			node->right = &nodeList[right - 'A'];
	}
	Node *root = &nodeList[0];
	preOrder(root);
	cout << "\n";
	inOrder(root);
	cout << "\n";
	postOrder(root);
	return 0;	
}
