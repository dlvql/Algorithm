#include <stdio.h>

int main() {
  char arr[100] = { "" };
  scanf("%s", arr);
  for(int i = 0; i < 100; i++) {
    if (arr[i] < 65 || arr[i] > 122) break;
    if (arr[i] < 97) printf("%c", arr[i] + 32);
    else printf("%c", arr[i] - 32);
  }
}