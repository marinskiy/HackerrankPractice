// Problem: https://www.hackerrank.com/challenges/c-tutorial-basic-data-types/problem
// Score: 10


#inculde <iostream>

int main() {
    int a;
    long b;
    char c;
    float d;
    double e;

    // get input with pointers
    scanf("%i %li %c %f %lf", &a, &b, &c, &d, &e);
    printf("%i\n%li\n%c\n%.03f\n%.09lf\n",a,b,c,d,e);

    return 0;
}
