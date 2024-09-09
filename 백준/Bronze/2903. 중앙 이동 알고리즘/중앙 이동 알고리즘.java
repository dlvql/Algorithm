import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int l = 1;
        for (int i = 0; i < n; i++) {
            l *= 2;
        }
        System.out.println((l + 1) * (l + 1));
    }
}