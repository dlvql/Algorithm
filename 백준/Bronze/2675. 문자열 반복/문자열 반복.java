import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for (int i = 0; i < t; i++) {
            int r = sc.nextInt();
            char[] str = sc.next().toCharArray();
            for (char c: str) {
                for (int j = 0; j < r; j++) {
                    System.out.print(c);
                }
            }
            System.out.println();
        }
    }
}