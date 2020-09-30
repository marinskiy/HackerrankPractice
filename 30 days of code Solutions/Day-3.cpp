#include <iostream>
using namespace std;


int main(){
    int N;
    cin >> N;
    if(N%2 != 0 || (N%2 == 0) && N >= 6 && N <= 20){
        cout << "Weird" << endl;
    }else cout << "Not Weird" << endl;
    return 0;
}
