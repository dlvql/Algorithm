import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        int cnt = 0;
        for (int i: arr) {
            for (int j = 2; j <= i; j++) {
                if (j == i) cnt++;
                else if (i % j == 0) break;
            }
        }
        System.out.println(cnt);
    }
}