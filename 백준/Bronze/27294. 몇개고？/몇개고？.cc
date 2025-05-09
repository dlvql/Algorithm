#include <stdio.h>

int main() {
    int t, s;
    scanf("%d %d", &t, &s);
    printf("%d", (t >= 12 && t <= 16 && s == 0) ? 320 : 280);
}