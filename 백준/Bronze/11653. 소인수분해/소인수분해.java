import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        if (n != 1) {
            for (int i = 2; 1 < n; ) {
                if (n % i == 0) {
                    System.out.println(i);
                    n /= i;
                } else {
                    i++;
                }
            }
        }
    }
}
