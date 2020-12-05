#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> l1={1, 2, 3, 4}, l2={5, 6, 7, 8}, l3;
    l3.resize(l1.size() + l2.size());
    merge(l1.begin(), l1.end(), l2.begin(), l2.end(), l3.begin());
    return 0;
}