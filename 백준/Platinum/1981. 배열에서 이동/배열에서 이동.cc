#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <climits>

using namespace std;

int n;
vector<vector<int>> l;
vector<pair<int, int>> dij = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

bool isin(int i, int j) {
    return 0 <= i && i < n && 0 <= j && j < n;
}

bool bfs(int x, int MIN, int MAX) {
    for (int m = MIN; m <= MAX - x; ++m) {
        if (!(m <= l[0][0] && l[0][0] <= m + x)) continue;

        vector<vector<bool>> visited(n, vector<bool>(n, false));
        queue<pair<int, int>> q;
        visited[0][0] = true;
        q.push({0, 0});

        while (!q.empty()) {
            auto [ui, uj] = q.front(); q.pop();
            if (ui == n - 1 && uj == n - 1) return true;

            for (auto [di, dj] : dij) {
                int vi = ui + di;
                int vj = uj + dj;

                if (!isin(vi, vj) || visited[vi][vj]) continue;
                if (m <= l[vi][vj] && l[vi][vj] <= m + x) {
                    visited[vi][vj] = true;
                    q.push({vi, vj});
                }
            }
        }
    }
    return false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n;
    l.resize(n, vector<int>(n));

    int MIN = INT_MAX;
    int MAX = INT_MIN;

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> l[i][j];
            MIN = min(MIN, l[i][j]);
            MAX = max(MAX, l[i][j]);
        }
    }

    int start = 0, end = MAX - MIN;
    while (end > start) {
        int mid = (start + end) / 2;
        if (bfs(mid, MIN, MAX)) {
            end = mid;
        } else {
            start = mid + 1;
        }
    }

    cout << end << '\n';
    return 0;
}
