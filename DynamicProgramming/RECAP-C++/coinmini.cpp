#include <iostream>
#include <vector>
#include<limits>
using namespace std;

int Inf =100000;

int recursion_solve(int sum,vector<int> arr)
{
    if(sum<0)
    {
        return Inf;
    }
    if(sum==0){
        return 0;
    }
    int best=Inf;
    for(int i=0;i<(int)arr.size();i++){
        best=min(best,recursion_solve(sum-arr[i],arr)+1);
    }
    return best;
}


int main()
{
    int n,sum;
    cin>>n>>sum;
    vector<int> arr(n);
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    cout<<"recursive solution = "<<recursion_solve(sum,arr)<<"\n";
    return 0;
}