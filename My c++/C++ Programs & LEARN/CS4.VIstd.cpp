#include<iostream>
using namespace std;
void primechk(int a)
{
	int j;
	if(a==0||a==1)
	{
		cout<<"NEITHER PRIME NOR COMPOSITE"<<endl;
	}
	else
	{
		for(j=2;j<a;j++)
		{
			if(a%j==0)
			{
				cout<<"COMPOSITE"<<endl;
				break;
			}
		}
		if(j==a)
		{
			cout<<"PRIME"<<endl;
		}
	}
}
void fibo(int n)
{
	int a=-1,b=1,c;
	for(int i=1;i<=n;i++)
	{
		cout<<endl;
		c=a+b;
		cout<<c<<"\t";
		primechk(c);
		a=b;
		b=c;
	}
}
int main()
{
	int n;
	cout<<"ENTER A REQUIRED NUMBER OF FIBO TERMS :"<<endl;
	cin>>n;
	cout<<"FIBONACCISERIES"<<endl;
	fibo(n);
	
}
