#include <stdio.h>

int main() {
  int len = 0, score = 0, sum = 0, isRight = 0;
  scanf("%d", &len);
  for (int i = 0; i < len; i++) {
    scanf("%d", &isRight);
    if (isRight == 1) score += 1;
    else score = 0;

    sum += score;
  }

  printf("%d", sum);
}