#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

vector<string>sorted;

bool ascending(string i, string m){return i < m;}

void compute(vector<string> email, vector<string> name){
    for(int i = 0; i < email.size(); ++i){
        if(email[i].find("@gmail.com") != std::string::npos){
            sorted.push_back(name[i]);
        }
    }
    sort(sorted.begin(), sorted.end(), ascending);
}

int main(){
    vector<string>mails;
    vector<string>names;
    int N;
    cin >> N;
    for(int a0 = 0; a0 < N; a0++){
        string firstName;
        string emailID;
        cin >> firstName >> emailID;
        names.push_back(firstName);
        mails.push_back(emailID);
    }
    compute(mails, names);
    for(auto m : sorted){
        cout << m << endl;
    }
    return 0;
}
