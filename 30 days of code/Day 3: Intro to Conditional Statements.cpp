#include <bits/stdc++.h>

using namespace std;

int isEven(int num)
{
    return !(num & 1);
}


int main()
{
    int N;
    cin >> N;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    if(isEven(N)){
        if(N > 20){
        cout << "Not Weird" << endl;
        }
        else if (N >= 6 && N <= 20) {
        cout << "Weird" << endl;
        }
        else if (N >=2 && N <= 5) {
        cout << "Not Weird" << endl;
        }
    }
    else {
    cout << "Weird" <<endl;
    }

    return 0;
}
