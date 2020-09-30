#include <cmath>
#include <iostream>
#include <exception>
#include <stdexcept>
using namespace std;

//------------------------------------------------------------------

class Calculator{
    public:
    int power(int a, int b){
        if(a < 0){
            throw invalid_argument( "n and p should be non-negative" );
        }
        if(b < 0){
            throw invalid_argument( "n and p should be non-negative" );
        }
        return pow(a, b);
    }
};

//---------------------------------------------------------------------

int main()
{
    Calculator myCalculator=Calculator();
    int T,n,p;
    cin>>T;
    while(T-->0){
      if(scanf("%d %d",&n,&p)==2){
         try{
               int ans=myCalculator.power(n,p);
               cout<<ans<<endl; 
         }
         catch(exception& e){
             cout<<e.what()<<endl;
         }
      }
    }
    
}
