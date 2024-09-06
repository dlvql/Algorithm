import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int m = -1;
        int r = -1;
        int c = -1;
        for (int i = 1; i <= 9; i++) {
            for (int j = 1; j <= 9; j++) {
                int input = sc.nextInt();
                if (input > m) {
                    m = input;
                    r = i;
                    c = j;
                }
            }
        }
        System.out.println(m);
        System.out.print(r + " " + c);
    }
}