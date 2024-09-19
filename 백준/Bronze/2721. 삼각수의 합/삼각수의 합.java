import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for (int i = 0; i < t; i++) {
            int n = sc.nextInt();
            int w = 0;
            for (int k = 1; k <= n; k++) {
                int a = 0;
                for (int j = 1; j <= k + 1; j++) a += j;
                w += k * a;
            }
            System.out.println(w);
        }
    }
}