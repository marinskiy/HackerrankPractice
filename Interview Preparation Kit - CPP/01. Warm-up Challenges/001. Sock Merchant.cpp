// Problem: https://www.hackerrank.com/challenges/sock-merchant/problem
// Score: 10


#include <iostream>
using namespace std;


int main()
{
    int n;
    int element;
    int arr[101] = {0};
    int ans = 0;

    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> element;
        arr[element] ++;

        ans += arr[element] / 2;
        arr[element] = arr[element] % 2;
    }

    cout << ans << endl;
    return 0;
}
