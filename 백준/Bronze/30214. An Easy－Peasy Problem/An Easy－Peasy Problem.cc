#include <stdio.h>

int main() {
  int s, p;
  scanf("%d %d", &s, &p);
  printf(s >= (double) p / 2 ? "E" : "H");
}