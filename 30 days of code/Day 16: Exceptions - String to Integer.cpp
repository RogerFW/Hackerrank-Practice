#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream> //只需要这一个，我也不知道为什么hackerrank要这么多其他的
#include <algorithm>
#include <unordered_map>
#include <cstdint>
#include <cinttypes>

using namespace std;


int main(){  
    try {
        string str;
        cin >> str;

        int num = stoi(str);
        cout << num;
    }
    catch (exception) {
        cout << "Bad String";
    }
}
