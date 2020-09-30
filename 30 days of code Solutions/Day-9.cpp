#include <iostream>

using namespace std;

int factorial(int y)
{
    if (y == 1){
        return 1;
    }
    else{
        return y * factorial(y - 1);
    }
}

int main() {
    int x;
    cin >> x;
    cout << factorial(x) << endl;
    return 0;
}
