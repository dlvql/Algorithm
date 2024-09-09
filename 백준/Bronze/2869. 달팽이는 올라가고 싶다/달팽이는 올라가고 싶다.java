import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int v = sc.nextInt();
        int d = ((v - a) / (a - b)) + 1;
        d += ((v - a) % (a - b)) != 0 ? 1 : 0;

        System.out.println(d);
    }
}