import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt(), b = sc.nextInt(), c = sc.nextInt();
        int d = sc.nextInt(), e = sc.nextInt(), f = sc.nextInt();
        int x = 0, y = 0;
        if (a == 0 && b != 0) {
            y = c / b;
            x = (f - (e * y)) / d;
        } else if (a != 0 && b == 0) {
            x = c / a;
            if (e != 0) y = (f - (e * x)) / e;
            else y = 0;
        } else if (a != 0 && b != 0) {
            y = (c * d - a * f) / (b * d - a * e);
            x = (f - (e * y)) / d;
        }
        System.out.println(x + " " + y);
    }
}