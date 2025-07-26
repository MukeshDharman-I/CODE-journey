// enum function in c++
#include<iostream>
using namespace std;
enum gender{male,female
};
int main()
{
	gender g = male;
	switch(g)
	{
		case male:
			cout<<"gender is male";
			break;
			case female:
				cout<<"gender is female";
				break;
				default:
					cout<<"invalid....";
					break;
	}
}
