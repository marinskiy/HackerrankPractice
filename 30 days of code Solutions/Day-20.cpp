#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


int calculate(vector<int> &ab)
{
	int allswaps = 0;
	while(1){
		int tempswaps = 0;
		for(int i = 0; i < ab.size() - 1; ++i){
			if(ab[i] > ab[i+1]){
				swap(ab[i], ab[i+1]);
				++tempswaps;
			}
		}
		if(tempswaps == 0){
			break;
		}
		allswaps += tempswaps;
	}
	return allswaps;
}

int main()
{
    int n;
    cin >> n;
    vector<int> a;
    for(int a_i = 0;a_i < n;a_i++){
       int p;
       cin >> p;
       a.push_back(p);
    }
    cout << "Array is sorted in " << calculate(a) << " swaps." << endl;
    cout << "First Element: " << a.at(0) << endl;
    cout << "Last Element: " << a.at(a.size() - 1) << endl;
    return 0;
}
