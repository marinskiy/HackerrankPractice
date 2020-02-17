// Problem: https://www.hackerrank.com/challenges/c-tutorial-strings/problem
// Score: 10

#include <iostream>
#include <string>

using std::cin;
using std::cout;
using std::endl;
using std::string;

int main() {

    string s1, s2;
    char c1, c2;

    // Get strings
    cin >> s1 >> s2;

    cout << s1.size() << " " << s2.size() << endl;
    cout << s1 + s2 << endl;

    // swap chars
    c1 = s1[0]; c2 = s2[0];
    s1[0] = c2; s2[0] = c1;

    cout << s1 << " " << s2 << endl;

    return 0;
}
