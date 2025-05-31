#include <stdio.h>

int main() {
  int t, a, b, c;
  scanf("%d", &t);
  for (int i = 0; i < t; i++) {
    scanf("%d %d %d", &a, &b, &c);
    printf("Case #%d: ", i + 1);
    if ((a + b) > c && (b + c) > a && (a + c) > b) {
      if ((a == b) && (b == c)) printf("equilateral");
      else if ((a == b) || (b == c) || (a == c)) printf("isosceles");
      else printf("scalene");
    }
    else printf("invalid!");
    printf("\n");
  }
}