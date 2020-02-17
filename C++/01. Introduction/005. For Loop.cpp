// Problem: https://www.hackerrank.com/challenges/c-tutorial-for-loop/problem
// Score: 10


#include <iostream>

using std::cin;
using std::cout;
using std::endl;
using std::string;

int main() {
    string nums[9] = {
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    };
    
    int start, end;
    cin >> start >> end;
    
    for (int i = start; i <= end; i++) {
        if (i <= 9) {
            cout << nums[i - 1] << endl;
        } else if (i % 2 == 0) {
            cout << "even" << endl;
        } else {
            cout << "odd" << endl;
        }
    } 
    
    return 0;
}
