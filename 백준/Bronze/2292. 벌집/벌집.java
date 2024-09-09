import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int ans = 1;
        for (int j = 1; j < n; ans ++) {
            j += 6 * ans;
        }
        System.out.println(ans);
    }
}