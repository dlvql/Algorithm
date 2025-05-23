#include <stdio.h>

int main() {
  char arr[3] = { "" };
  double score = 0;
  scanf("%s", arr);
  score = 69 - arr[0];
  if(arr[1] == '+') score += 0.3;
  else if (arr[1] == '-') score -= 0.3;
  if(arr[0] == 'F') score = 0;
  printf("%.1lf", score);
}