#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int nodes;
    cin >> nodes;
    vector <pair<int,int>> adj(nodes);

    for(int i=0;i<nodes;i++)
    {
        int edge,weight;
        cin>>edge>>weight;
        adj[i]={edge,weight};
    }

    return 0;
}
