// Problem: https://www.hackerrank.com/challenges/variable-sized-arrays/problem
// Score: 30

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n;
    int q;
    cin >> n >> q;
    vector<int> a[n];
    for(int i = 0; i < n; i++){
        int m;
        cin >> m;
        int o;
        for(int j = 0; j < m; j++){
            cin >> o;
            a[i].push_back(o);
        }
    }

    int r, s;
    for(int k = 1; k <= q; k++){
        cin >> r >> s;
        cout << a[r][s] << endl;
    }
    return 0;
}
