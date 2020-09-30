#include <iostream>
#include <vector>
#include <string>
using namespace std;


int main() {
    int x;
    cin >> x;
    map<string, string> all;
    for(int i = 0; i < x; ++i){
        string s, p;
        cin >> s >> p;
        all[s] = p;
    }
    string h;
    while(cin >> h){
        if(all.find(h) == all.end()){
            cout << "Not found" << endl;
        }
        else{
            cout << h << "=" << all.at(h) << endl;
        }
    }
}
