#include<stdio.h>

int main() {
  int tree, w, v;
  scanf("%d", &tree);
  scanf("%d %d", &w, &v);
  if ((double) w / v >= tree) printf("1");
  else printf("0");
}