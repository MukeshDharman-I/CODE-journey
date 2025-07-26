// diamond problem in c++
/*                          

                                                      __________________
                                                      
                                                           CLASS A
                                                      __________________
                                                      
                                                     ^                  ^
                                                    /                    \ 
                                                   /                      \
                                                  /                        \  
                                                 /                          \
                                                /                            \
                            _________________                                   __________________                  
                                             
							    CLASS B				                                 CLASS C
							__________________                                  __________________
		                                 ^					                     ^
							              \                                     /                       
							               \                                   /
							                \                                 /                                     AMBIGUOUS ERROR
							                 \                               /
							                  \                             /
							                   \                           / 
							                          _______________________
							                         
							                                CLASS D
							                         _______________________
*/
/* ambiguous error will appear because , B and C access the data of A and D access the data of B and C , 
   but when D tries to access the data of A (because it will think that "whether i have to go by B or C to access the data of A"), there error will apear .
   to clear that error an easy way is in the below program */ 
#include<iostream>
using namespace std;
class A
{
	 public :
	 	void display()
	 	{
	 		cout<<"display the method in A . "<<endl;
		 }
};
class B : virtual public A          // to get rid of this error , we have to use the keyword "virtual". so the way to cure this problem is to virtually inherit
{
	public :
		void show()
		{
			cout<<"show method in B . "<<endl;
		}
};
class C : virtual public A             // this is the way to cure this error
{
	
};
class D : public B, public C
{
	
};
int main()
{
	D o;
	o.display();
}							                      
