#include <iostream>
#include <string>
using namespace std;


int main() {
    int n;
    cin >> n;
    for(int i = 0; i < n; ++i){
        string m;
        cin >> m;
        for(int k = 0; k < m.size(); k +=2){
            cout << m[k];
        }
        cout << " ";
        for(int t = 1; t < m.size(); t +=2){
            cout << m[t];
        }
        cout << endl;
    }
    return 0;
}
