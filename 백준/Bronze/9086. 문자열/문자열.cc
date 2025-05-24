#include <stdio.h>

int main() {
  int t = 0, j;
  scanf("%d", &t);
  char arr[t][1000];
  for (int i = 0; i < t; i++){
    scanf("%s", arr[i]);
    printf("%c", arr[i][0]);
    for (j = 0; j < 998; j++) {
      if(arr[i][j + 1] < 65 || arr[i][j + 1] > 90) break;
    }
    printf("%c\n", arr[i][j]);
  }
}