#include <iostream>
#include <vector>

using namespace std;

int outAnd(int a, int b){
    vector<int>lol;
    for(int i = 1; i <= a; ++i){
        lol.push_back(i);
    }
    int max = 0;
    for(int i = 0; i < lol.size(); ++i){
        for(int p = i + 1; p < lol.size(); ++p){
            int anded = lol[i] & lol[p];
            if((anded > max) && (anded < b) ){
                max =  anded;
            }
        }
    }
    return max;
}

int main(){
    int t;
    cin >> t;
    for(int a0 = 0; a0 < t; a0++){
        int n;
        int k;
        cin >> n >> k;
        cout << outAnd(n, k) << endl;
    }
    return 0;
}
