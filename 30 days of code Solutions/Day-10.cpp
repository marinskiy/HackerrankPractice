#include <iostream>
#include <vector>
#include <algorithm>
#include <bitset>

using namespace std;

bool desc(int i, int l){return (i > l);}

int main(){
    int n;
    cin >> n;
    vector<int> ones;
    bitset<32> m(n);
    string ip = m.to_string();
    int cnt = 0;
    for(int m = 0; m < ip.size(); ++m){
        if(ip[m] == '1'){
            ++cnt;
        }
        else{
            ones.push_back(cnt);
            cnt = 0;
        }
        if(m == ip.size() - 1){
            ones.push_back(cnt);
        }
    }
    sort(ones.begin(), ones.end(), desc);
    cout << ones.at(0) << endl;
    return 0;
}
