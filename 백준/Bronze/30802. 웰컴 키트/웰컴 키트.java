import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] sizes = new int[6];
        int sum = 0;
        for (int i = 0; i < 6; i++) sizes[i] = sc.nextInt();
        int t = sc.nextInt(), p = sc.nextInt();
        for (int i : sizes) sum += (int) Math.ceil((double) i / t);
        System.out.println(sum);
        System.out.println((int) Math.floor((double) n / p) + " " + (n % p));
    }
}