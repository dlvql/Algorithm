#include<stdio.h>

int main() {
  int max = 0, idx = -1, a;
  for (int i = 0; i < 9; i++) {
    scanf("%d", &a);
    if (a > max) {
      max = a;
      idx = i + 1;
    }
  }
  printf("%d\n%d", max, idx);
}