// constructor overloading in c++
#include<iostream>
using namespace std;
class math
{
	private:
		int a,b,c;
		public:
			math() // default constructor
			{
				a=0;
				b=0;
			}
			math (int x,int y) // parameterized constructor
			{
				a=x;
				b=y;
			}
			math(math &x) // copy constructor
			{
				a=x.a;
				a=x.b;
			}
			void add()
			{
				c=a+b;
				cout<<"total : "<<c<<endl;
			}
};

int main()
{
	math o1;
	math o2 (100,43);
	math o3(o2);
	o1.add();
	o2.add();
	o3.add();
}
