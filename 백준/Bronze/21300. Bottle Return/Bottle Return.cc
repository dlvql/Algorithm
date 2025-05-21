#include<stdio.h>

int main() {
  int n, sum = 0;
  for (int i = 0; i < 6; i++) {
    scanf("%d", &n);
    sum += n * 5;
  }
  printf("%d", sum);
}