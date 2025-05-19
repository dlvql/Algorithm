#include<stdio.h>

int main() {
  int a, b, c;
  scanf("%d %d %d", &a, &b, &c);
  printf("%d\n", a + b - c);
  if (10 > b) printf("%d", a * 10 + b - c);
  else if (100 > b) printf("%d", a * 100 + b - c);
  else if (1000 > b) printf("%d", a * 1000 + b - c);
  else printf("%d", a * 10000 + b - c);
}