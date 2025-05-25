#include<stdio.h>

int main() {
  char arr[20];
  int t, r;
  scanf("%d", &t);
  for (int i = 0; i < t; i++) {
    scanf("%d %s", &r, arr);
    for (int j = 0; j < 20; j++) {
      if (arr[j] < 36 || arr[j] > 90) break;
      else if (arr[j] > 37 && arr[j] < 42) break;
      else if (arr[j] == 44) break;
      else if (arr[j] > 58 && arr[j] < 65) break;
      for (int k = 0; k < r; k++) {
        printf("%c", arr[j]);
      }
    }
    printf("\n");
  }
}