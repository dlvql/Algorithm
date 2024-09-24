import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] stack = new int[n];
        int top = -1;
        StringBuilder ans = new StringBuilder();
        for (int i = 0; i < n; i++) {
            int cmd = sc.nextInt();
            if (cmd == 1) {
                int x = sc.nextInt();
                top += 1;
                stack[top] = x;
            } else if (cmd == 2) {
                if (top < 0) ans.append("-1\n");
                else {
                    ans.append(stack[top]).append("\n");
                    top -= 1;
                }
            } else if (cmd == 3) {
                ans.append(top + 1).append("\n");
            } else if (cmd == 4) {
                ans.append(top < 0 ? 1 : 0).append("\n");
            } else {
                if (top >= 0) ans.append(stack[top]).append("\n");
                else ans.append("-1\n");
            }
        }
        System.out.print(ans);
    }
}