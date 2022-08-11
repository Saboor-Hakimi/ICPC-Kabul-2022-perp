#include <bits/stdc++.h>

using namespace std;



int main(){
    io::sync_with_stdio(false);

    int n,m;
    cin >> n >> m;
    vector<int> a(n);
    for(int i = 0; i<n; i++) cin >> a[i];
    vector<int> b(m);
    for(int i = 0; i<m; i++) cin >> b[i];

    a.push_back(INT_MAX);
    m.push_back(INT_MAX);

    int i = 0, j = 0;
    vector<int> c(n+m);

    while(i<n || j < m){
    if(j==m || (i<n && a[i] < b[j])){
        if(a[i] < b[j]){
            
        c[k++] = a[j++];

    } else {
        c[k++] = b[j++];
        }
    }
    for(int x: c){
        count << x << " ";

    }
    }
    cout << "\n";




}