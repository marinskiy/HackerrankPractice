#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<vector<int> >lmao;
vector<int> answers;

bool desc(int i, int k){return i > k;}

int TakeInput(int i, int m)
{
	for(int f = 0; f < i; ++f){
		vector<int> temp;
		for(int a = 0; a < m; ++a){
			int x;
			cin >> x;
			temp.push_back(x);
		}
		lmao.push_back(temp);
	}
	return 0;
}

void compute()
{
	for(int i = 0; i < lmao.size() - 2; ++i){
		for(int e = 0; e < lmao[i].size() - 2; ++e){
			int sum = lmao[i][e] + lmao[i][e+1] + lmao[i][e+2] + lmao[i+1][e+1] +lmao[i+2][e] + lmao[i+2][e+1] + lmao[i+2][e+2];
			answers.push_back(sum);
		}
	}
}
int main()
{
	TakeInput(6, 6);
	compute();
	sort(answers.begin(), answers.end(), desc);
	cout << answers.at(0) << endl;
}
