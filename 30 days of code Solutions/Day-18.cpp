#include <iostream>
#include <vector>
#include <deque>

using namespace std;

class Solution {
    private:
    vector<char>stack;
    deque<char>queue;
    int p = 0;
    int q = 0;
    public:
    char pushCharacter(char c){
       stack.push_back(c);
       return NULL;
    }
    char enqueueCharacter(char c){
        queue.push_front(c);
        return NULL;
    }
    char popCharacter(){
        return stack[p++];
    }
    char dequeueCharacter(){
        return queue[q++];
    }

};
