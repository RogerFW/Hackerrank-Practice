#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;
    
    vector<int> a(n);
    vector<int> w(n);
    
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    
    for (int i = 0; i < n; i++) {
        cin >> w[i];
    }
    
    double sum = 0;
    double cnt = 0;
    
    for (int i = 0; i < n; i++) {
        sum += a[i] * w[i];
        cnt += w[i];
    }
    
    double wmean = sum / cnt;
    
    printf("%.1f", wmean);
    
    return 0;
}
