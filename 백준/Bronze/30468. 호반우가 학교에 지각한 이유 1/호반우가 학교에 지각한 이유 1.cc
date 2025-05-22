#include<stdio.h>
int main() {
  int s, d, i, l, n;
  scanf("%d %d %d %d %d", &s, &d, &i, &l, &n);
  printf("%d", s + d + i + l >= n * 4 ? 0 : n * 4 - (s + d + i + l));
}