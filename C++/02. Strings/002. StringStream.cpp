// Problem: https://www.hackerrank.com/challenges/c-tutorial-stringstream/problem
// Score: 10

#include <sstream>
#include <vector>
#include <iostream>

using std::cin;
using std::cout;
using std::endl;
using std::string;
using std::stringstream;
using std::vector;

vector<int> parseInts(string str) {
    stringstream ss(str);
    char ch; int val;
    vector<int> ints;
    // extract integers
    while(ss >> val) {
        ints.push_back(val);
        ss >> ch;
    }
    return ints;
}

int main() {
    string str;
    cin >> str;
    vector<int> integers = parseInts(str);
    for(int i = 0; i < integers.size(); i++) {
        cout << integers[i] << "\n";
    }

    return 0;
}
