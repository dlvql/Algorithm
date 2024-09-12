import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long n = sc.nextLong();
        long cnt = 0;
        for (long i = 1; i <= n - 2; i++) {
            cnt += ((i + 1) * i) / 2;
        }
        System.out.println(cnt);
        System.out.println(3);
    }
}