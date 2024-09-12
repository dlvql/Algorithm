import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x_min = 10001, x_max = -10001, y_min = 10001, y_max = -10001;
        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            int x = sc.nextInt(), y = sc.nextInt();
            if (x < x_min) x_min = x;
            if (x > x_max) x_max = x;
            if (y < y_min) y_min = y;
            if (y > y_max) y_max = y;
        }
        System.out.println((x_max - x_min) * (y_max - y_min));
    }
}