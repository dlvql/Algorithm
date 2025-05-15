#include <stdio.h>

int main() {
  int a, b;
  scanf("%d %d", &a, &b);
  printf("%.15lf", (double) a / b);
}