#include<stdio.h>

int main() {
  int n, min = 1000000, max = -1000000, a;
  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    scanf("%d", &a);
    if (min > a) min = a;
    if (max < a) max = a;
  }
  printf("%d %d", min, max);
}