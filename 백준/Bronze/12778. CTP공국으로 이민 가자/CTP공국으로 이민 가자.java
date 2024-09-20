import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for (int i = 0; i < t; i++) {
            int m = sc.nextInt();
            char c = sc.next().charAt(0);
            if (c == 'C') {
                for (int j = 0; j < m; j++) {
                    System.out.print((sc.next().charAt(0) - 'A' + 1) + " ");
                }
            } else {
                for (int j = 0; j < m; j++) {
                    System.out.print(((char) (sc.nextInt() + 'A' - 1)) + " ");
                }
            }
            System.out.println();
        }
    }
}