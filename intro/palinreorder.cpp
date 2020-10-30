#include<bits/stdc++.h>
using namespace std;
int main()
{
    string st;
    int hash[26]={0};
    cin>>st;
    int n=st.length();
    for(int i=0;i<n;i++)
    {
        hash[st[i]-'A']++;
    }
    int flag=1;
    int count=0;
    for(int i=0;i<26;i++)
    {
        if(hash[i]%2!=0)
        {
            count++;
        }
        if(count>1)
        {
             cout<<"NO SOLUTION";
             flag=0;
            break;
        }
    }
    string st1;
    string ch;
    if(flag)
    {
        for(int i=0;i<26;i++)
        {
            if(hash[i]>=2 && hash[i]%2==0)
            {
                hash[i]=hash[i]/2;
                while(hash[i])
                {
                    st1+=char(i+'A');
                    hash[i]--;
                }
            }
            else if(hash[i]%2==1)
            {
                while(hash[i])
                {
                    ch+=char(i+'A');
                        hash[i]--;
                }
            }
        }
    }
    string st2=st1;
    int n1=st1.length();
    reverse(st1.begin(),st1.end());
    cout<<st2+ch+st1;
    
    
}