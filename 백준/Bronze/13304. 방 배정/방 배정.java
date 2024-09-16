import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), k = sc.nextInt();
        int[] m = new int[5];
        // 1~2
        // 3~4 여 0
        // 3~4 남 1
        // 5~6 여 0
        // 5~6 남 1
        for (int i = 0; i < n; i++) {
            int s = sc.nextInt();
            int y = sc.nextInt();
            if (y == 1 || y == 2) {
                m[0]++;
            } else if (y == 3 || y == 4) {
                if (s == 0) m[1]++;
                else m[2]++;
            } else if (y == 5 || y == 6) {
                if (s == 0) m[3]++;
                else m[4]++;
            }
        }
        int rooms = 0;
        for (int i: m) {
            rooms += (i / k) + (i % k == 0 ? 0 : 1);
        }
        System.out.println(rooms);
    }
}