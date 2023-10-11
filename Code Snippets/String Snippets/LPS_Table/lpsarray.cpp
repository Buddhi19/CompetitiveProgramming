#include <bits/stdc++.h>

using namespace std;

//counting boarders

vector<int> lps_array(string s){
    int i=0;
    int j=1;
    vector<int> lps(s.size());
    lps[0]=0;
    int count=0;
    while(j<(int)s.size()){
        if(s[j]==s[i]){
            count+=1;
            lps[j]=count;
            i+=1;
            j+=1;
        }
        else if(s[j]!=s[i]){
            i=0;
            if(s[j]==s[i]){
                count=0;
                continue;
            }
            count=0;
            lps[j]=count;
            j+=1;
        }
    }
    return lps;
}



int main()
{
    string s;
    cin>>s;    
    vector<int> ans=lps_array(s);
    for(int i=0;i<(int)ans.size();i++){
        cout<<ans[i]<<" ";
    }
    cout<<endl;
    return 0;
}