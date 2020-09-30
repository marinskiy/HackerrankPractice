#include <iostream>
#include <vector>

using namespace std;

//---------------------------------------------------------

template<typename TP> 
void printArray(vector<TP> array) {
     for(TP i : array){
          cout << i << endl;
     }
}

//-----------------------------------------------------

int main() {
  
    vector<int> vInt{1, 2, 3};
    vector<string> vString{"Hello", "World"};
    
    printArray<int>(vInt);
    printArray<string>(vString);
    
    return 0;
}
