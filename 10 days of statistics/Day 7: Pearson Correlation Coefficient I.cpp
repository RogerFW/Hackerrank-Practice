#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <iomanip>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n;
    cin >> n;
    vector<double> x, y;
    for (int i = 0; i < 2 * n; i++) {
        double val;
        cin >> val;
        if (i < n)
            x.push_back(val);
        else
            y.push_back(val);
    }
    double sum_x;
    double sum_y;
    double sum;
    double sigma_x;
    double sigma_y;
    double mean_x;
    double mean_y;
    double stdDev_x;
    double stdDev_y;
    double Person;
    int i;
    for (i = 0; i < n; i++) {
        sum_x += x[i];
        sum_y += y[i];
    }
    mean_x = sum_x / n;
    mean_y = sum_y / n;
    for (i = 0; i < n; i++) {
        sigma_x += pow(abs(x[i] - mean_x), 2)/n;
        sigma_y += pow(abs(y[i] - mean_y), 2)/n;
    }    
    stdDev_x = sqrt(sigma_x);
    stdDev_y = sqrt(sigma_y);
    for (int i = 0; i < n; i++){
        sum += (x[i] - mean_x) * (y[i] - mean_y);
    }
    Person = sum/(n * stdDev_x * stdDev_y);
    cout << fixed << setprecision(3) << Person << endl;
    return 0;
}
