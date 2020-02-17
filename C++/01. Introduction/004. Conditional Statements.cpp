// Problem: https://www.hackerrank.com/challenges/c-tutorial-conditional-if-else
// Score: 10


#include <iostream>

using std::cout;
using std::cin;
using std::endl;
using std::string;

int main () {
    string nums[10] = {
        "Greater than 9",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine"
    };
    
    int n;
    
    cin >> n;
    
    if (n <= 9) {
        cout << nums[n] << endl;
    } else {
        cout << nums[0] << endl;
    }
    
    return 0;
}
