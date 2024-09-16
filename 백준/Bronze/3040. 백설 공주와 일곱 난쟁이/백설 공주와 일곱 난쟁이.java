import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] arr = new int[9];
        int[] not = new int[2];
        int sum = 0;
        for (int i = 0; i < 9; i++) {
            int a = sc.nextInt();
            sum += a;
            arr[i] = a;
        }
        sum -= 100;
        for (int i = 0; i < 9; i++) {
            for (int j = i + 1; j < 9; j++) {
                if (i == j) continue;
                if (sum == arr[i] + arr[j]) {
                    not[0] = i;
                    not[1] = j;
                }
            }
        }
        for (int i = 0; i < 9; i++) {
            if (i == not[0] || i == not[1]) continue;
            System.out.println(arr[i]);
        }
    }
}