import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        int cnt = arr[n - 1] < arr[0] ? 0 : 1;
        for (int i = 1; i < n; i++) {
            if(arr[i] <= arr[i - 1]) {
                cnt++;
            }
        }
        System.out.println(cnt);
    }
}