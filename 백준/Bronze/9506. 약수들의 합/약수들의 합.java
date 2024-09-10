import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true) {
            int n = sc.nextInt();
            if (n == -1) {
                break;
            }
            int[] arr = new int[(int) (Math.sqrt(n) * 2 + 1)];
            int sum = 0;
            for (int i = 1, j = 0; i < n; i++) {
                if (n % i == 0) {
                    sum += i;
                    arr[j] = i;
                    j++;
                }
            }
            if (sum == n) {
                System.out.print(n + " = " + arr[0]);
                for (int i = 1; i < arr.length; i++) {
                    if (arr[i] != 0) {
                        System.out.print(" + " + arr[i]);
                    }
                }
                System.out.println();
            } else {
                System.out.println(n + " is NOT perfect.");
            }
        }
    }
}