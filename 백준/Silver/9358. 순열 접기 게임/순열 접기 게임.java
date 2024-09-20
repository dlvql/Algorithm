import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for (int i = 0; i < t; i++) {
            int n = sc.nextInt();
            int[] arr = new int[n];
            for (int j = 0; j < n; j++) {
                arr[j] = sc.nextInt();
            }
            while (n != 2) {
                if (n % 2 == 1) {
                    for (int idx = 0; idx < (n - 1) / 2; idx++){
                        arr[idx]  = arr[idx] + arr[n - 1 - idx];
                    }
                    arr[(int) Math.ceil((double) n / 2) - 1] += arr[(int) Math.ceil((double) n / 2) - 1];
                } else {
                    for (int idx = 0; idx < n / 2 - 1; idx++) {
                        arr[idx] = arr[idx] + arr[n - 1 - idx];
                    }
                }
                n = (int) Math.ceil((double) n / 2);
            }
            System.out.print("Case #" + (i + 1) + ": ");
            if (arr[0] > arr[1]) System.out.println("Alice");
            else System.out.println("Bob");
        }

    }
}