#include<bits/stdc++.h>
using namespace std;

int main()
{
    int n,a;
    cin>>n;
    vector<int>adj[n];
    for(int i=0;i<n;i++)
    {
        cin>>a;
        a--;
        adj[i].push_back(a);
    }
     vector<int>visited(n);
     vector<int>cycle(n);
    
    for(int i=0;i<n;i++)
    {
         int countt=0;
       
        
       queue<int>pq;
       pq.push(i);
       int flag=0;
  set<int>set;
  if(!visited[i])
  {
    //   cout<<"visited"<<i<<endl;
       while(!pq.empty())
       {
           int u=pq.front();
       set.insert(u);
            visited[u]=1;
            countt++;
           pq.pop();
           for(auto ele:adj[u])
           {
            
               
              if(!visited[ele])
              {
                   
                    pq.push(ele);
              }
                else
                {
                    for(auto it=set.begin();it!=set.end();it++)
                    {
                        if(*it!=ele)
                        cycle[*it]=countt+cycle[ele];
                        
                    }
                    cycle[ele]=countt;
                    flag=1;
                    break;
                }
           }
           
          if(flag)
            break;
       }
  }


    
       
      cout<<cycle[i]<<" ";
        
    }
    return 0;
}