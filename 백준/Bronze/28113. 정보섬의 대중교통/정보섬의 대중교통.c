#include <stdio.h>

int main() {
  int a, b, n;
  scanf("%d %d %d", &n, &a, &b);
  if (a == b) printf("Anything");
  else if (a > b) printf("Subway");
  else printf("Bus");
}