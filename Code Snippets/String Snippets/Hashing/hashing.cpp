#include <bits/stdc++.h>

using namespace std;

//######################### HASHING

long long compute_hash(string const& s){
    const int p=31; //for both lower and upper case 53 is good
    const long int MOD=1e9+9;
    long long hash_value=0;
    long long p_pow=1;
    for(auto c:s){
        hash_value=(hash_value+(c-'a'+1)*p_pow)%MOD;
        p_pow=(p_pow*p)%MOD;
    }
    return hash_value;
}


//################search for duplicate strings in an array of strings


vector<vector<int>> identical_strings(vector<string> const& s){
    // {"sw","dw","sw","edced","de"}--->{{0,2},{1,4},{3}}
    int n=s.size();
    vector<pair<long long,int>> hashes(n);
    for(int i=0;i<n;i++){
        hashes[i]={compute_hash(s[i]),i};
    }
    sort(hashes.begin(),hashes.end());

    vector<vector<int>> ans;
    for(int i=0;i<n;i++){
        if(i==0 || hashes[i].first!=hashes[i-1].first){
            ans.emplace_back();
        }
        ans.back().push_back(hashes[i].second);
    }
    return ans;
}


// count unique substrings



int main()
{
    int n;
    cin>>n;
    vector<string> s(n);
    for(int i=0;i<n;i++){
        cin>>s[i];
    }
    vector<vector<int>> ident=identical_strings(s);
    for(int i=0;i<(int)ident.size();i++){
        for(int j=0;j<(int)ident[i].size();j++){
            cout<<ident[i][j]<<" ";
        }
        cout<<"\n";
    }
    
    return 0;
}