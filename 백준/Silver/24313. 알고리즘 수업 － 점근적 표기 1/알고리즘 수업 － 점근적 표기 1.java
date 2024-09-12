import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a1 = sc.nextInt(), a0 = sc.nextInt();
        int c = sc.nextInt();
        int n0 = sc.nextInt();
        int ans = 1;
        for (int n = n0; n <= 100; n++) {
            if ((a1 * n + a0) > c * n) {
                ans = 0;
                break;
            }
        }
        System.out.println(ans);
    }
}