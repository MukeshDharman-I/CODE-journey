/*
basic class example
1. area of a circle
2. circumference of a circle
*/
#include<iostream>
using namespace std;
class circle
{
    private:
	        float radius;
	public:
			float area()
		{
			// area of circle is pi*radius*radius
			cout<<"enter the value of radius :";
			cin>>radius;
			return(3.14*(radius*radius));	
	    }
	    
			float circumference()
			{
		    //formula for circumference of a circle is 2*pi*r
		    return(2*3.14*(radius));
			}
};
int main()
{
	circle o;
	// creating an object o , using that object o we call area function 
	//as area is in public there is no problem is calling the function
	cout<<"area of the circle : "<<o.area()<<endl;
	cout<<"_____________________________________________"<<endl;
	cout<<"circumference of the circle : "<<o.circumference()<<endl;
	
}

