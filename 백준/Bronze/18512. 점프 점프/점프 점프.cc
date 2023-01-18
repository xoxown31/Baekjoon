#include <iostream>
using namespace std;

int x, y, p1, p2, i, j;

int main() {
  cin>>x>>y>>p1>>p2;	//1)

 while(1)
  {
    if(p1>p2)		//2)
      p2+=y;
      
    else if(p1<p2)	//3)
      p1+=x;
      
    else		//4)
    {
      cout<<p1;
      break;
    } 

    if(p1>10000 || p2>10000)	//5)
    {
      cout<<-1; 
      break;
    }
  }
}