// wht is a destructor
/* destructor is a instance member function which is invoked automatically
   whenever an object is goig to destroy
*/
#include <iostream>
using namespace std;
class math
{
private:
	int a,b,c;
	public:
		math ()
		{
			a=10;
			b=20;
		}
		~math() // this is the symbol for destructor (~)
		{
			cout<<"memory destroyed .."; // i have written , just to show that this {~math()} is enough to destroy the memory
		}
		void add()
		{
			c=a+b;
			cout<<"total : "<<c<<endl;
		}
};
int main()
{
	math o;
	o.add();
   }   
