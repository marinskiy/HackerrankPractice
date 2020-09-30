#include <iostream>
#include <cstddef>
#include <queue>
#include <string>
#include <cstdlib>

using namespace std;	
class Node{
    public:
        int data;
        Node *left,*right;
        Node(int d){
            data=d;
            left=right=NULL;
        }
};
class Solution{
    public:
  		Node* insert(Node* root, int data){
            if(root==NULL){
                return new Node(data);
            }
            else{
                Node* cur;
                if(data<=root->data){
                    cur=insert(root->left,data);
                    root->left=cur;
                }
                else{
                   cur=insert(root->right,data);
                   root->right=cur;
                 }           
           return root;
           }
        }
        
//-----------------------------------------------------------------------------------

	void levelOrder(Node *root){
      int height = MaxHeight(root);
        for(int i = 0; i <= height; ++i){
            ThisLevelTransversal(root, i);
        }
	}
    int MaxHeight(Node* root){
          if(root == NULL){
              return -1;
          }
          int ldepth = MaxHeight(root->left);
          int rdepth = MaxHeight(root->right);
          if(ldepth < rdepth){
              return (rdepth + 1);
          }else {return ldepth +1;}
        }
    void ThisLevelTransversal(Node *root, int level){
        if(root == NULL){return;}
        if (level == 0){
            cout << root->data << " ";
        }else if (level > 0){
            ThisLevelTransversal(root->left, level-1);
            ThisLevelTransversal(root->right, level-1);
        }
        
    }
    
//-------------------------------------------------------

};//End of Solution
int main(){
    Solution myTree;
    Node* root=NULL;
    int T,data;
    cin>>T;
    while(T-->0){
        cin>>data;
        root= myTree.insert(root,data);
    }
    myTree.levelOrder(root);
    return 0;
}
