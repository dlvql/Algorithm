#include <stdio.h>

int main() {
  char arr[102];
  int len;
  scanf("%s", arr);
  for (int i = 0; i < 102; i++) {
    if (arr[i] < 65 || arr[i] > 90 && arr[i] < 97 || arr[i] > 122 ) {
      len = i;
      break;
    }
  }
  printf("%d", len);
}