#include <bits/stdc++.h>
#define N 1000000
#define M 10000000

using namespace std;

struct Node {
	Node *next;
	int el;
	Node(int el, Node *next) {
		if(next == nullptr)
			this->next = this;
		else {
			this->next = next;
		}
		this->el = el;
	}
	Node* append(int el) {
		next = new Node(el, next);
		return next;
	}
};

Node **nodes = new Node*[N+1];

int main() {
	vector<int> input;
	string s;
	cin >> s;
	for(auto u:s) {
		input.push_back(u-'0');
	}
	for(int i=0; i<input.size(); i++) {
		if(i == 0) {
			nodes[input[i]] = new Node(input[i], nullptr);
		} else {
			nodes[input[i]] = nodes[input[i-1]]->append(input[i]);
		}
	}
	nodes[input.size()+1] = nodes[input[input.size()-1]]->append(input.size()+1);
	for(int i=input.size()+2; i<=N; i++)
		nodes[i] = nodes[i-1]->append(i);
	Node *cur = nodes[input[0]];
	for(int i=0; i<M; i++) {
		Node *s = cur->next;
		Node *e = cur->next->next->next;
		cur->next = e->next;
		int dest = cur->el;
		do {
			dest--;
			if(dest == 0)
				dest = N;
		} while(dest == s->el || dest == s->next->el || dest == e->el);
		e->next = nodes[dest]->next;
		nodes[dest]->next = s;
		cur = cur->next;
	}
	cur = nodes[1];
	cout << (((long long)cur->next->el)*(cur->next->next->el));
}
