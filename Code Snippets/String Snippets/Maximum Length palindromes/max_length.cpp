#include <bits/stdc++.h>

using namespace std;

int factorial(int n)
{
    int ans = 1;
    for (int i = 1; i <= n; i++)    
        ans = ans * i;
    return (ans);
}

long int numberOfPossiblePalindrome(string str, int n){
    long int MOD=1e9+7;
    unordered_map<char, int> mp;
    for (int i = 0; i < n; i++) 
        mp[str[i]]++;
 
    int k = 0;
    int num = 0;
    int den = 1;
    int fi;  
    for (auto it = mp.begin(); it != mp.end(); ++it)
    {
        if (it->second % 2 == 0){ 
            fi = it->second / 2;
        }
        else
        {
            fi = (it->second - 1) / 2; 
            k++;
        }
        num = num + fi; 
        den = den * factorial(fi); 
    }
    if (num != 0) 
        num = factorial(num);
         
    int ans = (num / den)%MOD; 
     
    if (k != 0)
    {
        ans = (ans * k)%MOD;
    }
    return (ans);
}

int main()
{
    string s;
    cin>>s;
    
    int n;
    cin>>n;
    while(n--){
        int a,b;
        cin>>a>>b;
        string new1=s.substr(a-1,b);
        cout<<numberOfPossiblePalindrome(new1,new1.size())<<endl;
    }
    
    return 0;
}