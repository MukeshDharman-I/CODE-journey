// write a c++ prog to chect percentage of a student and display the division ( distinction,first,second,third or fail) scored using switch case
/*
           PERCENTAGE          DIVISION
            >=80                distinction
            >=60 and <80        first division
            >=50 and <60        second division  
            >=40 and <50        third division
            <40                 fail
*/
#include<iostream>
using namespace std;
int main()
{
	int x;
	float percent;
	cout<<"ENTER THE PERCENTAGE YOU SCORED :"<<endl;
	cin>>percent;
	cout<<"YOU HAVE SCORED "<<percent<<" % :"<<endl;
	x=percent/10;
	switch(x)
	{
		case 10:
		case 9:
		case 8:
		cout<<"YOU HAVE PASSED WITH DISTINCTION..."<<endl;
		break;
		case 7:
		case 6:
		cout<<"YOU HAVE PASSED WITH FIRST DIVISION..."<<endl;
		break;	
		case 5:
		cout<<"YOU HAVE PASSED WITH SECOND DIVISION..."<<endl;
		break;
		case 4:
		cout<<"YOU HAVE PASSED WITH THIRD DIVISION..."<<endl;
		break;
		default :
		cout<<"SORRY, YOU HAVE FAILED ._.?"<<endl;	
	}
}
