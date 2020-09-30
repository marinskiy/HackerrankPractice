#include <iostream>
using namespace std;


int main() {
    double x, y, z;
    cin >> x >> y >> z;
    double tip = x * y / 100;
    double tax = x * z / 100;
    double total = x + tip + tax;
    int total2 = total;
    cout << "The total meal cost is " << total2 << " dollars.";
    
}
