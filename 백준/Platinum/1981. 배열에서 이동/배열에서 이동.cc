#include <iostream>
#include <queue>

using namespace std;

const int MAXSIZE = 100;

int MAX = 0;
int MIN = 200;

int n;
int l[MAXSIZE+1][MAXSIZE+1];

int dij[4][2] = {
    {0,1},
    {0,-1},
    {1,0},
    {-1,0}
};

bool f(int mid);
bool bfs(int mid, int x);

int main() {
    cin >> n;

    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            cin >> l[i][j];
            MAX = max(MAX, l[i][j]);
            MIN = min(MIN, l[i][j]);
        }
    }

    int start = 0, end = MAX - MIN;
    while(end > start){
        int mid = (start+end) / 2;
        if(f(mid)) end = mid;
        else start = mid+1;
    }

    cout << end;

    return 0;
}

bool f(int mid){
    for(int x = MIN; mid+x <= MAX; x++){
        if(bfs(mid, x)) return true;
    }
    return false;
}

bool bfs(int mid, int x){
    int visited[MAXSIZE+1][MAXSIZE+1] = {false};
    queue <pair <int, int>> q;

    if (!(x <= l[0][0] && l[0][0] <= mid+x)) return false;

    visited[0][0] = true;
    q.push({0,0});

    while(!q.empty()){
        auto [ui, uj] = q.front(); q.pop();

        if(ui == n-1 && uj == n-1) return true;

        for(auto [di, dj] : dij){
            int vi = ui + di;
            int vj = uj + dj;

            if(!(0 <= vi && vi < n && 0 <= vj && vj < n)) continue;
            if(!(x <= l[vi][vj] && l[vi][vj] <= mid+x)) continue;
            if(visited[vi][vj]) continue;

            q.push({vi,vj});
            visited[vi][vj] = true;

        }
    }
    return false;
}