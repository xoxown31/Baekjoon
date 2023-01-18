#include <stdio.h>
#include <math.h>

int main(void) {
	int a, b, c, i = 0;
	while (1){
		scanf("%d %d %d", &a, &b, &c);
		if(a==0 && b==0 && c==0) break;
		i++;
		printf("Triangle #%d\n", i);
		if(a==0 || b==0 || c==0) printf("Impossible.\n\n");
		else if(a==-1){
			if(c*c-b*b > 0) printf("a = %.3f\n\n", sqrt(c*c - b*b));
			else printf("Impossible.\n\n");
		}
		else if(b==-1){
			if(c*c-a*a > 0) printf("b = %.3f\n\n", sqrt(c*c - a*a));
			else printf("Impossible.\n\n");
		}
		else if(c==-1){
			if(a*a+b*b > 0) printf("c = %.3f\n\n", sqrt(a*a + b*b));
			else printf("Impossible.\n\n");
		}
	}
	return 0;
}