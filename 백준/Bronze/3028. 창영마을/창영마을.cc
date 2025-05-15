#include<stdio.h>

int main() {
  char arr[50];
  int cups[3] = {1, 0, 0}, temp = 0;
  scanf("%s", arr);
  for (int i = 0; i < 50; i++) {
    if (arr[i] == 'A') {
      temp = cups[0];
      cups[0] = cups[1];
      cups[1] = temp;
    }
    else if (arr[i] == 'B') {
      temp = cups[1];
      cups[1] = cups[2];
      cups[2] = temp;
    }
    else if (arr[i] == 'C') {
      temp = cups[0];
      cups[0] = cups[2];
      cups[2] = temp;
    }
  }

  if (cups[0] == 1) printf("1");
  else if (cups[1] == 1) printf("2");
  else if (cups[2] == 1) printf("3");
}