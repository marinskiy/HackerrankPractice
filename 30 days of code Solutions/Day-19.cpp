#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
class AdvancedArithmetic{
    public:
        virtual int divisorSum(int n)=0;
};

//--------------------------------------------------------------------

class Calculator : public AdvancedArithmetic{
    public:
    int divisorSum(int n){
        vector<int>divisors;
        for(int i = 1; i <= n; ++i){
            if(n % i == 0){
                divisors.push_back(i);
            }
        }
        int sum = 0;
        for(auto m : divisors){
            sum += m;
        }
        return sum;
    }
};

//---------------------------------------------------------------

int main(){
    int n;
    cin >> n;
    AdvancedArithmetic *myCalculator = new Calculator(); 
    int sum = myCalculator->divisorSum(n);
    cout << "I implemented: AdvancedArithmetic\n" << sum;
    return 0;
}
