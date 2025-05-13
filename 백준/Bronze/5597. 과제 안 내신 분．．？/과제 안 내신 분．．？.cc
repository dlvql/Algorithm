#include <stdio.h>

int main() {
  int arr[30], v, ab[2] = {0, 0};
  for (int i = 0; i < 30; i++) arr[i] = 1;
  for (int i = 0; i < 28; i++) {
    scanf("%d", &v);
    arr[v - 1] = 0;
  }
  v = 0;
  for (int i = 0; i < 30; i++) {
    if (arr[i] == 1) {
      ab[v++] = i + 1;
    }
  }
  if (ab[0] > ab[1]) printf("%d\n%d", ab[1], ab[0]);
  else printf("%d\n%d", ab[0], ab[1]);
}