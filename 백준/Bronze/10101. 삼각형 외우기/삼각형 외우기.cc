#include <stdio.h>

int main() {
  int a, b, c;
  scanf("%d\n%d\n%d", &a, &b, &c);
  if (a == 60 && a == b && a == c) printf("Equilateral");
  else if (a + b + c == 180) {
    if (a == b || b == c || a == c) printf("Isosceles");
    else printf("Scalene");
  }
  else printf("Error");
}