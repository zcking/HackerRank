#include <iostream>
using namespace std;


int main() {
    int q, n;
    cin >> q;
    
    for (int i = 0; i < q; i++) {
        cin >> n;
        if (n % 2 == 0)
            cout << "Yes\n";
        else
            cout << "No\n";
    }
    return 0;
}
