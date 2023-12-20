#include <iostream>

using namespace std;

int main()
{
    /*for (int i = 0; i * i < 1000000000; i++)
        cout << i << endl; // O(sqrt n)

    for (int i = 0; i < 1000; i++)
        cout << i << endl; // O(n)*/

    for (unsigned long long int i = 1000000000000000; i > 0; i /= 2)
        cout << i << endl;
}