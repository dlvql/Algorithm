import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int[] arr = new int[(int) Math.floor(Math.sqrt(n)) * 2 + 1];
        int ans = 0;
        int cnt = 0;
        for (int i = 1; i <= n; i++) {
            if (n % i == 0) {
                cnt++;
                arr[cnt] = i;
                if (cnt == k) {
                    ans = i;
                    break;
                }
            }
        }
        System.out.println(ans);
    }
}