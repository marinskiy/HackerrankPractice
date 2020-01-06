// Problem: https://www.hackerrank.com/challenges/sock-merchant/problem
// Score: 10

#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int n;
    int element;
    int arr[100] = {0};
    int ans = 0;

    std::cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> element;
        arr[element - 1] ++;

        ans += arr[element - 1] / 2;
        arr[element - 1] = arr[element - 1] % 2;
    }

    std::cout << ans;

    return 0;
}
