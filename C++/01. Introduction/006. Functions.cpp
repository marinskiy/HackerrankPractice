// Problem: https://www.hackerrank.com/challenges/c-tutorial-functions
// Score: 10


#include <iostream>

using std::cin;
using std::cout;
using std::endl;

int greatest(int a, int b, int c, int d) {
    return ((a>b?a:b)>(c>d?c:d)?(a>b?a:b):(c>d?c:d));
}

int main() {
    int a, b, c, d;
    cin >> a >> b >> c >> d;
    cout << greatest(a, b, c, d) << endl;
    
    return 0;
}
