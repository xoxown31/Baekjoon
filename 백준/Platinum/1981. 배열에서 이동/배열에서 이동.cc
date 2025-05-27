#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int MAX = 0;
int MIN = 200;
const int MAXSIZE = 100;

int n;
int l[MAXSIZE][MAXSIZE];

int dij[4][2] = {
    {1, 0},
    {-1, 0},
    {0, -1},
    {0, 1}
};

bool isin(int i, int j);

void input();
void solve();

bool f(int x);
bool bfs(int x, int m);

bool isin(int i, int j){
    return 0 <= i && i < n && 0 <= j && j < n;
}

void input() {
    cin >> n;

    for(int i=0; i<n; i++){
        for(int j = 0; j < n; j++){
            cin >> l[i][j];
            MAX = max(l[i][j], MAX);
            MIN = min(l[i][j], MIN);
        }
    }
}

void solve(){
    int start = 0, end = MAX - MIN;
    while(end > start){
        int mid = (start + end) / 2;
        if(f(mid)) end = mid;
        else start = mid + 1;
    }

    cout << end << '\n';
    return;
}

bool f(int x){
    for(int m = MIN; m < MAX - x + 1; m++){
        if(bfs(x, m)) return true;
    }
    return false;
}

bool bfs(int x, int m){
    if(!(m <= l[0][0] && l[0][0] <= m+x)) return false;

    bool visited[MAXSIZE+1][MAXSIZE+1] = {false};
    queue<pair<int, int>> q;

    visited[0][0] = true;
    q.push({0, 0});

    while(!q.empty()){
        auto [ui, uj] = q.front(); q.pop();
        if(ui == n-1 && uj == n-1) return true;

        for(auto [di, dj] : dij){
            int vi = ui + di;
            int vj = uj + dj;

            if (!isin(vi, vj) || visited[vi][vj]) continue;
            if (m <= l[vi][vj] && l[vi][vj] <= m+x){
                visited[vi][vj] = true;
                q.push({vi,vj});
            }
        }
    }

    return false;
}

int main() {
    input();
    solve();
}