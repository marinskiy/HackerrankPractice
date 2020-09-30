#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

bool CheckPrime(int n){
    if(n == 1){return false;}
    int m;
    m = sqrt(n);
    bool isprime = true;
    for(int i = 2; i <= m; ++i){
        if(n % i == 0){
            isprime = false;
            break;
        }
    }
    return isprime;
}

int main() {
    int p;
    cin >> p;
    for(int i = 0; i < p; ++i){
        int m;
        cin >> m;
        if(CheckPrime(m)){
            cout << "Prime" << endl;
        }else cout << "Not prime" << endl;
    }
    return 0;
}
