#include<stdio.h>

int main() {
    char a[1000];
    int s;
    scanf("%s", a);
    scanf("%d", &s);
    printf("%c", a[s - 1]);
}