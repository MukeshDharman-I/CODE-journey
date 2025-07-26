#include<iostream>
using namespace std;
int main()
{
	int rev=0,digit,n,num;
	cout<<"ENTER A POSITIVE NUMBER :"<<endl;
	cin>>num;
	n=num;
	while(num)
	{
	digit=num%10;
	rev=(rev*10)+digit;
	num=num/10;
    }
    cout<<"THE REVERSE OF THE GIVEN NUMBER :"<<rev<<endl;
    if(n==rev)
    cout<<"THE NUMBER IS A PALINDROME..."<<endl;
    else
    cout<<"THE NUMBER IS NOT A PALINDROME..."<<endl;
}
