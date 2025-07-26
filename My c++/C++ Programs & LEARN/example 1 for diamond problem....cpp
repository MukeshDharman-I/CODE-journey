//example for diamond problem in c++
#include<iostream>
using namespace std;
class a
{
	public :
	a()                                                               // constructor must be in public
	{
		cout<<"constructing a "<<endl;                                // using constructor 
	}
};
class b : virtual public a
{
	public :
	b()
   	{                                                                  // i have used virtual in a and b because during the execution of my output i am getting two a
		cout<<"constructing b "<<endl;                                 // the program is getting confused because when i execute d , d executes b and c , where both inherits a
		                                                               // to avoid this silly confusing mistake we use virtual in b and c
	}                                                                  // if we use virtual constructor it will not allow to make a copy
};
class c : virtual public a
{
	public :
	c()
	{
		cout<<"constructing c "<<endl;
	}
};
class d :public b, public c
{
	public :
	d()
	{
		cout<<"counstructing d "<<endl;
	}
};
int main()
{
	d o;                                       // we are having two "constructing a" in our output
	                                           // to avoid that we are going to use virtual inheritance
}
