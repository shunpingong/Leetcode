#include <stdio.h>
#include <stdlib.h>

int *r;

int fib(int n){
    r = calloc(n+1,sizeof(int));
    for (int i=0; i<=n;i++){
        if (i==0){
            r[0] = 0;
        }
        else if (i==1){
            r[1] = 1;
        }
        else{
            r[i] = r[i-1]+r[i-2];
        }
    }
    return r[n];
}