// Problem: https://www.hackerrank.com/challenges/c-tutorial-pointer
// Score: 10


#include <stdio.h>

void update(int *a, int *b) {
    int sum = *a + *b;
    int diff = *a - *b > 0 ? *a - *b : -(*a - *b);
    *a = sum;
    *b = diff;
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}
