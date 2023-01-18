#include<iostream>
#include<map>

using namespace std;

int dx[] = {0, 1, 1, 0, -1, -1};
int dy[] = {2, 1, -1, -2, -1, 1};

map<pair<int, int>, bool> visited;
int c = 0;

void backtrack(int x, int y, int dir, int n){
    if(n==0){
        if(visited.find({x, y}) != visited.end()) ++c;
        return;
    }

    if(visited.find({x, y}) != visited.end()) return;
    
    visited[{x, y}] = true;

    int dir_right = (dir+1)%6;
    int dir_left = (dir+5)%6;

    backtrack(x+dx[dir_right], y+dy[dir_right], dir_right, n-1);
    backtrack(x+dx[dir_left], y+dy[dir_left], dir_left, n-1);

    visited.erase({x, y});

    return;
}

int main(){

    int N;
    cin >> N;

    visited[{0, 0}] = true;
    backtrack(0, 2, 0, N);

    cout << c;

    return 0;
}