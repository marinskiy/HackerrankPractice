// Problem: https://www.hackerrank.com/challenges/2d-array/problem
// Score: 15


#include <cstdio>
#include <iostream>
#include <climits>
int main() {
    int m[6][6];


    for (int i = 0; i < 6; ++i) {
        for (int j = 0; j < 6; ++j) {
            std:: cin >> m[i][j];
        }
    }
     long temp_sum = 0, MaxSum = LONG_MIN;
    for (int i = 0; i < 6; ++i) {
        for (int j = 0; j < 6; ++j) {
            if (j + 2 < 6 && i + 2 < 6) {
                temp_sum = m[i][j] + m[i][j + 1] + m[i][j + 2] + m[i + 1][j + 1] + m[i + 2][j] + m[i + 2][j + 1] + m[i + 2][j + 2];
                if (temp_sum >= MaxSum) {
                    MaxSum = temp_sum;
                }
            }
        }
    }
    std:: cout << MaxSum;
    return 0;
}
