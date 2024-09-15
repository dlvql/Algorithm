import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        for (int i = 2; ; i++) {
            for (int j = 1; j < i; j++) {
                if (x == ((i - 2) * (i - 1) / 2) + j) {
                    if (i % 2 == 1) System.out.println(j + "/" + (i - j));
                    else System.out.println((i - j) + "/" + j);
                    return;
                }
            }
        }
    }
}