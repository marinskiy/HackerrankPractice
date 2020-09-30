#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int fine;
    int retDay, retMonth, retYear;
    int expDay, expMonth, expYear;
        cin >> retDay >> retMonth >> retYear;
        cin >> expDay >> expMonth >> expYear;
    if(retYear < expYear){
        fine = 0;
    }else if(retYear == expYear){
        if(retMonth < expMonth){
            fine = 0;
        }else if(retMonth == expMonth){
            if(retDay <= expDay){
                fine = 0;
            }else fine = (retDay - expDay) * 15;
        }else fine = (retMonth - expMonth) * 500;
    }else fine = 10000;
    cout << fine << endl;
    return 0;
}
