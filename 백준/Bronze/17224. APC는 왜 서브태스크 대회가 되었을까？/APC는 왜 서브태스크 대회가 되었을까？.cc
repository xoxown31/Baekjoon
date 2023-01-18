#include <stdio.h>
#include <functional>
#include <algorithm>

#define MAXSIZE 100

using namespace std;

int readInt();

int N, L, K;
int sub[MAXSIZE][2];

void Input(){
    N = readInt();
    L = readInt();
    K = readInt();
    for(int i=0; i<N; i++){
        sub[i][0] = readInt();
        sub[i][1] = readInt();
    }
}

int score[MAXSIZE];

void Solve(){
    for(int i=0; i<N; i++){
        score[i] = 0;
        if(L >= sub[i][0]){
            score[i] += 100;
            if(L >= sub[i][1])
                score[i] += 40;
        }
    }

    sort(score, score+N, greater<int>());

    int Answer = 0;
    for(int i=0; i<K; i++){
        Answer += score[i];
    }
    printf("%d\n", Answer);

}

int main(){
    Input();
    Solve();
}

int readInt(){
    int temp;
    scanf("%d", &temp);
    return temp;
}