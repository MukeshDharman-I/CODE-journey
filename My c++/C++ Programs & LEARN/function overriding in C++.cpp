// function overriding in C++

#include<iostream>
using namespace std;
class base
{
protected:	
int a,b;                                               
public :
  void add ()
  {
  cout<<"\n enter two numberes : ";
  cin>>a>>b;
  cout<<"\n total : "<<a+b;	
  }                                  	
};
class derived : public base
{
	private :
		int c;                                                    // if we redefine the function (function which has the same name) of the base class in the derived class then it is called function overriding
	public :
	void add()
	{
	cout<<"\n enter three numbers : ";
	cin>>a>>b>>c;
	cout<<"\n the sum of three numbers : "<<a+b+c;	
	}	
};
int main()
{
	base o;
	o.add();
	derived d;
	d.add();
}
