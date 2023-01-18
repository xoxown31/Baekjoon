#include <stdio.h>
#include <memory.h>
#include <vector>
#include <queue>

#define MAXSIZE 200000

using namespace std;

int readInt();

int N, M;
vector<int> link[MAXSIZE+1];
vector<int> infected;

void GatherInput(){
    int temp;
    N = readInt();
    
    for(int i=1; i<=N; ++i){
        while(true){
            temp = readInt();
            if (temp == 0) break;
            link[i].push_back(temp);
        }
    }
    
    M = readInt();
    
    for(int i=0; i<M; ++i) infected.push_back(readInt());
}

int people[MAXSIZE+1] = {-1,};

void Solve(){
    queue<int> q;
    
    memset(people, -1, sizeof(people));
    
    for(int i=0; i<M; ++i) {
        people[infected[i]] = 0;
        q.push(infected[i]);
    }
    
    int u, v;
    
    while(!q.empty()){
        u = q.front(); q.pop();

        for(int i=0; i<link[u].size(); ++i){
            v = link[u][i];
            
            if (people[v] >= 0) continue;
            
            people[v] -= 1;
            if (-1*people[v] - 1 >= (link[v].size()+1)/2){
                people[v] = people[u] + 1;
                q.push(v);
            }
        }
    }
}

void Print(){
    for(int i=1; i<=N; ++i) printf("%d ", people[i] >= 0 ? people[i] : -1);
}

int main(){
    GatherInput();

    Solve();
    
    Print();
    
}

int readInt(){
    int temp;
    scanf("%d", &temp);
    return temp;
}