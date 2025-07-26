//write a c++ prog to input basic salary of an employee and calculate its gross salary according to following :
// basic salary <25000 : hra = 20% , da = 80%
// basic salary >+25000 : hra = 25% , da = 90%
// basic salary >=40000 : hra = 30% , da = 95%
#include<iostream>
using namespace std;
int main()
{
	int gross,basic,hra,da;
	cout<<"enter the basic salary of an employee : \n";
	cin>>basic;
	if(basic < 25000)
	{
		hra=basic*20/100;
		da=basic*80/100;
	}
	else if (basic >=25000 && basic < 40000)
	{
		hra=basic*25/100;
		da=basic*90/100;
	}
	else if (basic >=40000)
	{
		hra=basic*30/100;
		da=basic*95/100;
	}
	gross=basic+hra+da;
	cout<<"---------------------------------------------- "<<endl;
	cout<<"BASIC SALARY        : "<<basic<<endl;
	cout<<"HOME RENT ALLOWANCE : "<<hra<<endl;
	cout<<"DEARNESS ALLOWANCE  : "<<da<<endl;
	cout<<"---------------------------------------------- "<<endl;
	cout<<"GROSS SALARY        : "<<gross<<endl;
	cout<<"---------------------------------------------- "<<endl;
}
