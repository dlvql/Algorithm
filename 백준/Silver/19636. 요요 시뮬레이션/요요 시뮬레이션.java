import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int w0 = sc.nextInt(), l0 = sc.nextInt(), t = sc.nextInt();
        int d = sc.nextInt(), l = sc.nextInt(), a = sc.nextInt();

        int w1 = w0 + ((l - (a + l0)) * d);
        if (w1 <= 0) System.out.println("Danger Diet");
        else System.out.println(w1 + " " + l0);

        w1 = w0;
        int l1 = l0;
        for (int i = 0; i < d; i++) {
            if (l1 <= 0 || w1 <= 0) {
                System.out.println("Danger Diet");
                return;
            }
            w1 += l - (l1 + a);
            if (Math.abs(l - (a + l1)) > t) {
                l1 += Math.floorDiv((l - (l1 + a)), 2);
            }
        }
        if (w1 <= 0 || l1 <= 0) System.out.println("Danger Diet");
        else {
            System.out.print(w1 + " " + l1 + " ");
            if (l0 - l1 > 0) System.out.println("YOYO");
            else System.out.println("NO");
        }
    }
}