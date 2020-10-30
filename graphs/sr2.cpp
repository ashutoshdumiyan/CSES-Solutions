#include<bits/stdc++.h>
using namespace std;
using ll = long long;
ll INF = 1e18;
int main()
{
ios::sync_with_stdio(0);
  cin.tie(0);
    long long n,m,q,u,v,w;
    cin>>n>>m>>q;
    vector<vector<long long int>>dist(n,vector<long long int>(n,INF));
    
    
    while(m--)
    {
        cin>>u>>v>>w;
        u--;
        v--;
        if(dist[u][v]>w)
        {
        dist[u][v]=w;
        dist[v][u]=w;
        }
        
    }
    
    for(int k=0;k<n;k++)
    {
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)
            {
                dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j]);
            }
        }
    }

    while(q--)
    {
        
        cin>>u>>v;
        u--;
        v--;
        if(u==v)
            cout<<0<<endl;
        else if(dist[u][v]==INF)
            cout<<-1<<endl;
            
        else
        cout<<dist[u][v]<<endl;
    }
    
    return 0;
}