#include<bits/stdc++.h>
using namespace std;

const int N = 1e5+2;
bool graph[N];
vector<int>adjc[N];

int main()
{
    for(int i=0; i<N; i++)
        graph[i] = 0;

    int V,E;
    cin>> V >> E;
    int x,y;
    for(int i=0; i<E; i++)
    {
        cin>> x >> y;

        adjc[x].push_back(y);
        adjc[y].push_back(x);
    }
    queue<int>q;
    q.push(1);
    graph[1] = true;

    while(!q.empty())
    {
        int node=q.front();
        q.pop();
        cout << node << endl;
        vector<int> :: iterator t;
        for(t = adjc[node].begin(); t != adjc[node].end(); t++)
        {
            if(!graph[*t])
            {
                graph[*t]=1;
                q.push(*t);
            }
        }
    }
}
